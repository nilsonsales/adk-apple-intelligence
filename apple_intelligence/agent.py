from google.adk.agents import Agent

from google import genai


contacts = [
    {
        "name": "John Doe",
        "number": "+1234567890",
        "email": "johndoe@email.com",
        "address": "123 Main St, Springfield, USA",
        "date_of_birth": "1993-02-20"
    },
    {
        "name": "Jane Smith",
        "number": "+0987654321",
        "email": "janesmith@email.com",
        "address": "456 Elm St, Springfield, USA",
        "date_of_birth": "1988-07-10"
    },
    {
        "name": "Alice Johnson",
        "number": "+1122334455",
        "email": "",
        "address": "789 Oak St, Springfield, USA",
        "date_of_birth": "1990-06-12"
    },
    {
        "name": "Zac Wingate",
        "number": "+2233445566",
        "email": "",
        "address": "",
        "date_of_birth": "1995-03-30"
    }
]


calendar_events = [
    {
        "title": "Meeting with John Doe",
        "description": "Discuss project updates and next steps.",
        "date": "2023-10-01",
        "time": "10:00 AM",
        "location": "Conference Room A"
    },
    {
        "title": "Doctor's Appointment",
        "description": "Annual check-up.",
        "date": "2023-10-02",
        "time": "2:00 PM",
        "location": "Health Clinic"
    },
    {
        "title": "Dinner with Family",
        "description": "Family gathering.",
        "date": "2023-10-03",
        "time": "6:30 PM",
        "location": "Home"
    },
    {
        "title": "Production catch up",
        "description": "Discuss project milestones and deliverables with Zac Wingate.",
        "date": "2024-07-03",
        "time": "9:30 AM",
        "location": "Cafe Grenel"
    }
]

emails_list = [
    {
        "sender": "johndoe@email.com",
        "recipient": "janesmith@email.com",
        "subject": "Project Update",
        "date": "2023-10-01",
        "body": "Hi Jane, I wanted to update you on the project status..."
    },
    {
        "sender": "janesmith@email.com",
        "recipient": "johndoe@email.com",
        "subject": "Re: Project Update",
        "date": "2023-10-02",
        "body": "Thanks for the update, John. I appreciate it."
    },
    {
        "sender": "alicejohnson@email.com",
        "recipient": "johndoe@email.com",
        "subject": "Meeting Reminder",
        "date": "2023-10-03",
        "body": "Don't forget our meeting tomorrow at 10 AM."
    },
    {
        "sender": "zacwingate@email.com",
        "recipient": "janesmith@email.com",
        "subject": "Project catch up",
        "date": "2024-07-02",
        "body": "Hi Jane, I wanted to schedule a catch-up meeting to discuss the production status and next steps."
    },
    {
        "sender": "zacwingate@email.com",
        "recipient": "janesmith@email.com",
        "subject": "Updates on the project",
        "date": "2024-07-10",
        "body": "Hi Jane, my manager is inquiring about the production status and next steps. Can we schedule a meeting to discuss this?"
    }
]


def get_user_information(name: str) -> dict:
    """
    Returns information about a user in the database.

    Args:
        name (str): The name of the user to retrieve information for.

    Returns:
        dict: status and result or error msg.
    """

    result = [u for u in contacts if name.lower() in u.get("name").lower()]

    if len(result) == 0:
        return {"status": "error", "message": "User not found"}
    elif len(result) > 1:
        return {"status": "error", "message": "Too many users with this name. Please provide the full name"}
    else:
        return {"status": "success", "result": result[0]}
    

def list_all_users() -> list:
    """
    Returns a list of all users in the database.

    Returns:
        list: A list of dictionaries, where each dictionary represents a user in the database.
    """

    return [{"name": u.get("name")} for u in contacts]

def list_calendar_events() -> list:
    """
    Returns a list of all calendar events.

    Returns:
        list: A list of dictionaries, where each dictionary represents a calendar event.
    """

    return calendar_events

def list_events_by_location(location: str) -> list:
    """
    Returns a list of calendar events filtered by location.
    You can use this function to find events that occur at a specific location.

    Args:
        location (str): The location to filter events by.

    Returns:
        list: A list of dictionaries, where each dictionary represents a calendar event at the specified location.
    """

    return [event for event in calendar_events if event.get("location") and location.lower() in event.get("location").lower()]


def list_emails() -> list:
    """
    Returns a list of all emails.

    Returns:
        list: A list of dictionaries, where each dictionary represents an email.
    """

    return emails_list


def writer_assistant(prompt: str) -> str:
    """
    Uses the Gemini API to generate a response based on the provided prompt.

    Args:
        prompt (str): The input prompt for the Gemini model.

    Returns:
        str: The generated response from the Gemini model.
    """
    
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text.strip()


root_agent = Agent(
    name="apple_intelligence_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer general question about Apple's ecosystem."),
    instruction=(
        "You are a helpful agent called Siri who can answer user questions about their contacts and events and provide factual answers."
        "Use all available tools to retrieve the information needed to answer the user's question."
        "You first retrieve the information about the user from the contacts and calendar events and then answer the user's question."
        "If the users asks a complex question, try to break it down into smaller parts and use your tools to find an answer."
    ),
    tools=[list_all_users, get_user_information, list_calendar_events, list_events_by_location,
           list_emails, writer_assistant],  # Add the tools to the agent
)
