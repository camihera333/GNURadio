INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_INTERPOLATOR Interpolator)

FIND_PATH(
    INTERPOLATOR_INCLUDE_DIRS
    NAMES Interpolator/api.h
    HINTS $ENV{INTERPOLATOR_DIR}/include
        ${PC_INTERPOLATOR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    INTERPOLATOR_LIBRARIES
    NAMES gnuradio-Interpolator
    HINTS $ENV{INTERPOLATOR_DIR}/lib
        ${PC_INTERPOLATOR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(INTERPOLATOR DEFAULT_MSG INTERPOLATOR_LIBRARIES INTERPOLATOR_INCLUDE_DIRS)
MARK_AS_ADVANCED(INTERPOLATOR_LIBRARIES INTERPOLATOR_INCLUDE_DIRS)

