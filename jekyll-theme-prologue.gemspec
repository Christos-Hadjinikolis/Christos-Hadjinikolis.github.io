Gem::Specification.new do |spec|
  spec.name          = "jekyll-theme-prologue"
  spec.version       = "0.3.2"
  spec.authors       = ["HTML5 UP", "Chris Bobbe"]
  spec.email         = ["csbobbe@gmail.com"]

  spec.summary       = %q{A Jekyll version of the Prologue theme by HTML5 UP.}
  spec.description   = %q{A Jekyll version of the Prologue theme by HTML5 UP. Demo: https://chrisbobbe.github.io/jekyll-theme-prologue/}
  spec.homepage      = "https://github.com/chrisbobbe/jekyll-theme-prologue"
  spec.license       = "CC-BY-3.0"

  spec.metadata = {
    "source_code_uri" => "https://github.com/chrisbobbe/jekyll-theme-prologue",
    "documentation_uri" => "https://github.com/chrisbobbe/jekyll-theme-prologue#readme"
  }

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r{^(assets|_layouts|_includes|_sass|_sections|_posts|assets|feed\.xml|index\.md|.*\.html|Gemfile|Gemfile\.lock|Makefile|README\.md|LICENSE\.md|\.ruby-version)$}i) }
  spec.require_paths = ["lib"]

  # Specify which files should be added to the RubyGems package
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "jekyll", ">= 4.0", "< 5.0"
  spec.add_development_dependency "bundler", ">= 2.1", "< 3.0"
  spec.required_ruby_version = '>= 2.7', '< 4.0'

  # Include dependencies for your gem
  # Add runtime dependencies here with:
  # spec.add_runtime_dependency 'dependency', '~> version'

  # Add development dependencies here with:
  # spec.add_development_dependency 'dependency', '~> version'
end
