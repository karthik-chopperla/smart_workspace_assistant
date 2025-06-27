from datetime import datetime, timedelta
from typing import List, Dict


def generate_schedule(tasks_with_urgency: List[Dict]) -> List[Dict]:
    """
    Builds a simulated schedule using simple time-blocking logic.
    Prioritizes higher urgency first. Generates realistic time slots.
    """

    # Sort tasks by urgency (descending)
    sorted_tasks = sorted(tasks_with_urgency, key=lambda x: x['urgency'], reverse=True)

    schedule = []
    base_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    task_duration = timedelta(minutes=45)

    for i, task_info in enumerate(sorted_tasks):
        start_time = base_time + i * task_duration
        end_time = start_time + task_duration

        schedule.append({
            "task": task_info["task"],
            "urgency": task_info["urgency"],
            "time_slot": f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}"
        })

    return schedule


def reschedule_tasks(existing_schedule: List[Dict], feedback_data: Dict) -> List[Dict]:
    """
    Adjusts the urgency of tasks and regenerates the schedule based on feedback.
    """
    for item in existing_schedule:
        key = item["task"].lower()
        if key in feedback_data:
            item["urgency"] = feedback_data[key]  # override with new rating

    return generate_schedule(existing_schedule)
