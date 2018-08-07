INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RANGES Ranges)

FIND_PATH(
    RANGES_INCLUDE_DIRS
    NAMES Ranges/api.h
    HINTS $ENV{RANGES_DIR}/include
        ${PC_RANGES_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RANGES_LIBRARIES
    NAMES gnuradio-Ranges
    HINTS $ENV{RANGES_DIR}/lib
        ${PC_RANGES_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RANGES DEFAULT_MSG RANGES_LIBRARIES RANGES_INCLUDE_DIRS)
MARK_AS_ADVANCED(RANGES_LIBRARIES RANGES_INCLUDE_DIRS)

