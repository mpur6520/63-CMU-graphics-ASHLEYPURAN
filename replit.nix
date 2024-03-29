{ pkgs }: {
  deps = [
    pkgs.libxcrypt
    pkgs.pkg-config
    pkgs.cairo
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Neded for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for cmu_graphics
      pkgs.cairo
      pkgs.SDL2
      pkgs.xorg.libXi
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
  };
}