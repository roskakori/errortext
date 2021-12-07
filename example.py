import argparse

from errortext import error_text


def do_something(action_to_perform):
    if action_to_perform == "walk":
        print("walking")
    elif action_to_perform == "sleep":
        raise ValueError("must be tired in order to sleep")
    elif action_to_perform == "run":
        raise NotImplementedError("run")
    else:
        assert False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="example for errortext package")
    parser.add_argument("action_to_perform", metavar="ACTION", help="action to perform, for example: walk")
    args = parser.parse_args()

    action = args.action_to_perform
    try:
        do_something(action)
        print(f"Success: done with {action}")
    except Exception as error:
        print(f"Error with str       : cannot {action}: {str(error)}")
        print(f"Error with error_text: cannot {action}: {error_text(error)}")
