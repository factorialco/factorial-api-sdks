# frozen_string_literal: true

module F
  # The gem's single namespace on the shared F:: root (see api.rb).
  module Api
    # Cursor-based pagination for list endpoints.
    #
    # The pagination params (after_id, limit) are not in the OpenAPI spec but
    # work at runtime; they are injected via the generated methods'
    # `query_params:` passthrough.
    #
    #   pages = F::Api.paginate { |page| api.teams_team.teams_teams_get(query_params: page) }
    #   pages.each { |team| puts team.name }
    #   pages.to_a          # collect everything
    #   pages.first(10)     # stops fetching once it has 10
    # rubocop:disable Metrics/MethodLength -- one cohesive cursor loop; splitting it
    # further would scatter the enumerator's control flow across methods.
    def self.paginate(limit: nil, max_items: nil, &fetcher)
      Enumerator.new do |yielder|
        after_id = nil
        yielded  = 0

        # catch/throw is a plain non-local exit (not an exception): `throw :done`
        # unwinds straight to this catch block. A `return` here would raise
        # LocalJumpError because the enumerator block runs after paginate has
        # already returned.
        catch(:done) do
          loop do
            items, meta = extract_page(fetcher.call(page_params(limit, after_id)))

            items.each do |item|
              yielder << item
              yielded += 1
              throw :done if max_items && yielded >= max_items
            end

            break unless meta&.has_next_page && meta.end_cursor

            after_id = meta.end_cursor
          end
        end
      end
    end
    # rubocop:enable Metrics/MethodLength

    # Query params for a single page request.
    def self.page_params(limit, after_id)
      params = {}
      params[:limit] = limit if limit
      params[:after_id] = after_id if after_id
      params
    end

    # Splits a list response into its items and pagination metadata.
    def self.extract_page(response)
      items = response.respond_to?(:data) ? Array(response.data) : []
      meta  = response.respond_to?(:meta) ? response.meta : nil
      [items, meta]
    end

    private_class_method :page_params, :extract_page
  end
end
