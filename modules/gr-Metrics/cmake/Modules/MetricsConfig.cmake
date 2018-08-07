INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_METRICS Metrics)

FIND_PATH(
    METRICS_INCLUDE_DIRS
    NAMES Metrics/api.h
    HINTS $ENV{METRICS_DIR}/include
        ${PC_METRICS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    METRICS_LIBRARIES
    NAMES gnuradio-Metrics
    HINTS $ENV{METRICS_DIR}/lib
        ${PC_METRICS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(METRICS DEFAULT_MSG METRICS_LIBRARIES METRICS_INCLUDE_DIRS)
MARK_AS_ADVANCED(METRICS_LIBRARIES METRICS_INCLUDE_DIRS)

