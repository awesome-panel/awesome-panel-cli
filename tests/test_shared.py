"""We have shared functionality"""
from awesome_panel_cli import shared


def test_can_run_in_subprocess(mocker):
    """Can run command in subprocess"""
    # Givens
    spy = mocker.patch("subprocess.run")
    command = "echo hello"
    # When
    shared.run(command=command)
    # Then
    spy.assert_called_once_with("echo hello", check=True)
