require "cgi"

module SnippetTokens
  TOKEN = /\{\{\s*snippet:([a-zA-Z0-9_-]+)\s*\}\}/.freeze

  module_function

  def render(content, site, locale)
    return content unless content&.match?(TOKEN)

    content.gsub(TOKEN) do
      snippet_id = Regexp.last_match(1)
      snippet_path = File.join(site.source, "docs", "snippets", snippet_id, "#{locale}.code")
      fallback_path = File.join(site.source, "docs", "snippets", snippet_id, "en.code")
      resolved_path = File.exist?(snippet_path) ? snippet_path : fallback_path

      unless File.exist?(resolved_path)
        Jekyll.logger.warn("snippet_tokens:", "missing snippet #{snippet_id} for locale #{locale}")
        next "<!-- missing snippet #{snippet_id} for locale #{locale} -->"
      end

      snippet = File.read(resolved_path, encoding: "utf-8").rstrip
      escaped = CGI.escapeHTML(snippet)
      "\n<pre><code class=\"language-python\">#{escaped}</code></pre>\n"
    end
  end
end

Jekyll::Hooks.register [:pages, :documents], :pre_render do |doc|
  locale = doc.data["locale"] || "en"
  doc.content = SnippetTokens.render(doc.content, doc.site, locale)
end
