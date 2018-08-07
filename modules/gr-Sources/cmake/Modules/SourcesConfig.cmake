INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SOURCES Sources)

FIND_PATH(
    SOURCES_INCLUDE_DIRS
    NAMES Sources/api.h
    HINTS $ENV{SOURCES_DIR}/include
        ${PC_SOURCES_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SOURCES_LIBRARIES
    NAMES gnuradio-Sources
    HINTS $ENV{SOURCES_DIR}/lib
        ${PC_SOURCES_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SOURCES DEFAULT_MSG SOURCES_LIBRARIES SOURCES_INCLUDE_DIRS)
MARK_AS_ADVANCED(SOURCES_LIBRARIES SOURCES_INCLUDE_DIRS)

