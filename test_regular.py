import pytest
import subprocess
import signal


def input_data(proc, input):
    try:
        outs, errs = proc.communicate(input=input, timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()

    return outs, errs


def run_module(module_name):
    proc = subprocess.Popen(['python', module_name], )

    return proc


def test_run_terminate():

    p = run_module('regular')
    # TODO : make sure it has started ?
    p.terminate()
    p.wait(timeout=5)


@pytest.mark.skipif(condition=not hasattr(signal, 'SIGTERM'), reason="signal doesnt have CTRL_C_EVENT on this platform")
def test_run_sigterm():

    p = run_module('regular')
    # TODO : make sure it has started ?
    p.send_signal(signal.SIGTERM)
    p.wait(timeout=5)


@pytest.mark.skipif(condition=not hasattr(signal, 'CTRL_C_EVENT'), reason="signal doesnt have CTRL_C_EVENT on this platform")
def test_run_ctrlc():
    p = run_module('regular')
    # TODO : make sure it has started ?
    p.send_signal(signal.CTRL_C_EVENT)
    p.wait(timeout=5)


@pytest.mark.skipif(condition=not hasattr(signal, 'CTRL_C_EVENT'), reason="signal doesnt have CTRL_BREAK_EVENT on this platform")
def test_run_ctrlbreak():
    p = run_module('regular')
    # TODO : make sure it has started ?
    p.send_signal(signal.CTRL_BREAK_EVENT)
    p.wait(timeout=5)


if __name__ == '__main__':
    pytest.main([
        '-s', __file__,
])
