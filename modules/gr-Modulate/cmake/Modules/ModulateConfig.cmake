INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MODULATE Modulate)

FIND_PATH(
    MODULATE_INCLUDE_DIRS
    NAMES Modulate/api.h
    HINTS $ENV{MODULATE_DIR}/include
        ${PC_MODULATE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MODULATE_LIBRARIES
    NAMES gnuradio-Modulate
    HINTS $ENV{MODULATE_DIR}/lib
        ${PC_MODULATE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MODULATE DEFAULT_MSG MODULATE_LIBRARIES MODULATE_INCLUDE_DIRS)
MARK_AS_ADVANCED(MODULATE_LIBRARIES MODULATE_INCLUDE_DIRS)

