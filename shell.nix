{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    pyright
    # python311Packages.simple-websocket
    (python311.withPackages (ps: with ps; [
        flask
        flask-socketio
        simple-websocket
        eventlet
        pytest
    ]))

    nodejs_20
  ];

  shellHook = ''
    echo "Flask development environment activated!"
  '';
}
