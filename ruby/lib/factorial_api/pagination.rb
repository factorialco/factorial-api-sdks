# frozen_string_literal: true

module F
  # Cursor-based pagination for list endpoints.
  #
  # The pagination params (after_id, limit) are not in the OpenAPI spec but
  # work at runtime; they are injected via the generated methods'
  # `query_params:` passthrough.
  #
  #   pages = F.paginate { |page| api.teams_team.teams_teams_get(query_params: page) }
  #   pages.each { |team| puts team.name }
  #   pages.to_a          # collect everything
  #   pages.first(10)     # stops fetching once it has 10
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
          page_params = {}
          page_params[:limit]    = limit    if limit
          page_params[:after_id] = after_id if after_id

          response = fetcher.call(page_params)
          items    = response.respond_to?(:data) ? Array(response.data) : []
          meta     = response.respond_to?(:meta) ? response.meta : nil

          items.each do |item|
            yielder << item
            yielded += 1
            throw :done if max_items && yielded >= max_items
          end

          break unless meta&.has_next_page && meta&.end_cursor

          after_id = meta.end_cursor
        end
      end
    end
  end
end
