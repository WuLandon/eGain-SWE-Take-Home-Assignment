def handle_in_transit(tracking_info):
    """
    Handle the conversation path for a package that is still in transit.
    """

    print("Your package is currently in transit.")
    print(f"Estimated delivery: {tracking_info['estimated_delivery']}.")

    print("\nPlease check back if it does not arrive by the estimated delivery date.")


def handle_delayed(tracking_info, get_yes_no_response):
    """
    Handle the conversation path for a delayed package.
    """

    print("Your package has been delayed.")
    print(f"Estimated delivery: {tracking_info['estimated_delivery']}.")

    receive_updates = get_yes_no_response(
        "\nWould you like to receive delivery updates?"
    )

    if receive_updates:
        print("\nDelivery updates have been enabled.")
        print(
            "We'll notify you if there are any changes to your estimated delivery date."
        )
    else:
        print(
            "\nNo problem. You can check back anytime for the latest tracking information."
        )


def handle_delivered(tracking_info, get_yes_no_response):
    """
    Handle the conversation path for a package marked as delivered.
    """

    print(
        f"Tracking shows your package was delivered on {tracking_info['delivered_on']}."
    )

    print("I can help start a missing package investigation.\n")

    open_claim = get_yes_no_response("Would you like to open a missing package claim?")

    if open_claim:
        print("\nMissing package claim created.")
        print("A support specialist will follow up with you shortly.")
    else:
        print("\nNo claim was created.")
        print("You can return later if you still need help with this package.")
