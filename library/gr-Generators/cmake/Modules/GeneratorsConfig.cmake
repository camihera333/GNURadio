INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GENERATORS Generators)

FIND_PATH(
    GENERATORS_INCLUDE_DIRS
    NAMES Generators/api.h
    HINTS $ENV{GENERATORS_DIR}/include
        ${PC_GENERATORS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GENERATORS_LIBRARIES
    NAMES gnuradio-Generators
    HINTS $ENV{GENERATORS_DIR}/lib
        ${PC_GENERATORS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GENERATORS DEFAULT_MSG GENERATORS_LIBRARIES GENERATORS_INCLUDE_DIRS)
MARK_AS_ADVANCED(GENERATORS_LIBRARIES GENERATORS_INCLUDE_DIRS)

