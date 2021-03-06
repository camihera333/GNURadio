INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_INTERPOLATORS Interpolators)

FIND_PATH(
    INTERPOLATORS_INCLUDE_DIRS
    NAMES Interpolators/api.h
    HINTS $ENV{INTERPOLATORS_DIR}/include
        ${PC_INTERPOLATORS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    INTERPOLATORS_LIBRARIES
    NAMES gnuradio-Interpolators
    HINTS $ENV{INTERPOLATORS_DIR}/lib
        ${PC_INTERPOLATORS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(INTERPOLATORS DEFAULT_MSG INTERPOLATORS_LIBRARIES INTERPOLATORS_INCLUDE_DIRS)
MARK_AS_ADVANCED(INTERPOLATORS_LIBRARIES INTERPOLATORS_INCLUDE_DIRS)

