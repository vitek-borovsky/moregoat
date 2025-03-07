{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    pyright
    (python311.withPackages (ps: with ps; [
        flask
        flask-socketio
        simple-websocket
        eventlet
        pytest
    ]))

    nodejs_20
    tailwindcss

  ];

  shellHook = ''
    alias k="kubectl"
    echo "Flask development environment activated!"
  '';
}
