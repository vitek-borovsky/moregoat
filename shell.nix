{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    pyright
    (python311.withPackages (ps: with ps; [ flask ])) # Include Flask directly
  ];

  shellHook = ''
    echo "Flask development environment activated!"
  '';
}

