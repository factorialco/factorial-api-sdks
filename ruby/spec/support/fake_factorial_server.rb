# frozen_string_literal: true

require 'socket'

# Minimal single-threaded HTTP server on a random free port. Records every
# request it receives (request line + headers + body) and answers with
# whatever the `responder` block returns for it: a JSON string (served as
# 200), a [status, body] pair, or [status, body, content_type] for non-JSON
# responses.
class FakeFactorialServer
  EMPTY_PAGE = '{"data":[],"meta":{"end_cursor":null,"has_next_page":false,' \
               '"has_previous_page":false,"limit":100,"total":0}}'

  attr_reader :requests
  # Swappable per example, so one shared server can serve many responders.
  attr_writer :responder

  def initialize(&responder)
    @server = TCPServer.new('127.0.0.1', 0)
    @responder = responder || ->(_request_line, _body) { EMPTY_PAGE }
    @requests = []
    @thread = Thread.new { serve }
  end

  def base_url
    "http://127.0.0.1:#{@server.addr[1]}"
  end

  def stop
    @server.close
    @thread.join(1)
  end

  private

  def serve
    loop { handle(@server.accept) }
  rescue IOError, Errno::EBADF
    # server socket closed: shutting down
  end

  def handle(sock)
    request_line = sock.gets.to_s.chomp
    headers = {}
    while (line = sock.gets) && line != "\r\n"
      key, value = line.chomp.split(': ', 2)
      headers[key.downcase] = value
    end
    body = headers['content-length'] ? sock.read(headers['content-length'].to_i) : nil
    @requests << { line: request_line, headers: headers, body: body }

    status, payload, content_type = response_for(request_line, body)
    sock.write("HTTP/1.1 #{status} Status\r\nContent-Type: #{content_type}\r\n" \
               "Content-Length: #{payload.bytesize}\r\nConnection: close\r\n\r\n#{payload}")
    sock.close
  end

  def response_for(request_line, body)
    status, payload, content_type = @responder.call(request_line, body)
                                              .then { |result| result.is_a?(Array) ? result : [200, result] }
    [status, payload.to_s, content_type || 'application/json']
  end
end
