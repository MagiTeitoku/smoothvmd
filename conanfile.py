from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires('boost/[^1.85]')
        self.requires('icu/[^74.2]')
        self.requires('eigen/[^3.4]')
        self.requires('gtest/[^1.14]')

    def build_requirements(self):
        self.tool_requires("cmake/[^3.15]")
        
    def configure(self):
        BOOST_CONFIGURE_OPTIONS = (
            "atomic",
            "charconv",
            "chrono",
            "cobalt",
            "container",
            "context",
            "contract",
            "coroutine",
            "date_time",
            "exception",
            "fiber",
            "filesystem",
            "graph",
            "graph_parallel",
            "iostreams",
            "json",
            "locale",
            "log",
            "math",
            "mpi",
            "nowide",
            "program_options",
            "python",
            "random",
            "regex",
            "serialization",
            "stacktrace",
            "system",
            "test",
            "thread",
            "timer",
            "type_erasure",
            "url",
            "wave",
        )
        for opt in BOOST_CONFIGURE_OPTIONS:
            self.options["boost"].__setattr__(f"without_{opt}", True)
        self.options["boost"].__setattr__("header_only", False)
        for opt in ("filesystem", "system", "program_options", "atomic"):
            self.options["boost"].__setattr__(f"without_{opt}", False)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()