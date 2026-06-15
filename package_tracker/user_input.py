def has_tracking_number():
    """
    Determine whether the user has a tracking number.
    If not, provide guidance on where to find it.
    """

    has_tracking = get_yes_no_response("Do you have your tracking number?")

    if has_tracking:
        return True

    print("\nYou can usually find your tracking number in:")
    print("- Your shipping confirmation email")
    print("- Your order confirmation page")
    print("- Your carrier's mobile app")

    found_tracking = get_yes_no_response(
        "\nWere you able to locate your tracking number?"
    )

    if found_tracking:
        return True

    print("\nI’m unable to look up a package without a tracking number.")
    print("Please contact customer support with your order information.")

    return False


def get_tracking_number(tracking_data):
    """
    Prompt the user for a tracking number and continue prompting
    until the user enters a valid tracking number that exists.
    """

    tracking_number = input("Please enter your tracking number (e.g., 12345): ").strip()

    while True:
        if not (tracking_number.isdigit() and len(tracking_number) == 5):
            tracking_number = input(
                "\nInvalid tracking number.\n"
                "Please enter a valid 5-digit tracking number (e.g., 12345): "
            ).strip()
            continue

        if tracking_number not in tracking_data:
            tracking_number = input(
                "\nTracking number not found.\n"
                "Please check your tracking number and try again: "
            ).strip()
            continue

        return tracking_number


def get_yes_no_response(prompt):
    """
    Prompt the user until a valid yes/no response is received.
    """

    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()

        if response == "yes":
            return True

        if response == "no":
            return False

        print("Sorry, I didn't understand that.")
        print("Please answer with 'yes' or 'no'.\n")
