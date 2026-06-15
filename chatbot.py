from package_tracker.conversation_handlers import (
    handle_delayed,
    handle_delivered,
    handle_in_transit,
)
from package_tracker.messages import display_goodbye_message, display_welcome_message
from package_tracker.tracking_data import TRACKING_DATA
from package_tracker.user_input import (
    get_tracking_number,
    get_yes_no_response,
    has_tracking_number,
)


def main():
    display_welcome_message()

    if not has_tracking_number():
        display_goodbye_message()
        return

    tracking_number = get_tracking_number(TRACKING_DATA)

    tracking_info = TRACKING_DATA[tracking_number]

    status = tracking_info["status"]

    print(f"\nTracking Status: {status.replace('_', ' ').title()}")

    if status == "in_transit":
        handle_in_transit(tracking_info)

    elif status == "delayed":
        handle_delayed(tracking_info, get_yes_no_response)

    elif status == "delivered":
        handle_delivered(tracking_info, get_yes_no_response)

    display_goodbye_message()


if __name__ == "__main__":
    main()
