def check_and_decide(user_data: dict) -> dict:
    steps = []
    messages = []

    # Step 1: Check if user exists
    if not user_data.get("exists"):
        steps.append("create_user")
        messages.append(f"User {user_data.get('email')} not found → will create")
    else:
        messages.append(f"User {user_data.get('email')} exists ✅")

    # Step 2: Check license
    if not user_data.get("license_assigned"):
        steps.append("assign_license")
        messages.append("No license found → will assign license")
    else:
        messages.append("License already assigned ✅")

    # Step 3: Check role
    if not user_data.get("role_assigned"):
        steps.append("assign_role")
        messages.append("No role found → will assign role")
    else:
        messages.append("Role already assigned ✅")

    return {
        "user": user_data.get("email"),
        "actions_needed": steps,
        "summary": messages
    }