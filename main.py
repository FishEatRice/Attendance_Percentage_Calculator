import streamlit as st

def time_to_hours(hours, minutes):
    return hours + minutes / 60

def main():
    st.title("Attendance Percentage Calculator")
    
    # Create 3 columns for Practical, Tutorial, Lecturer
    col1, col2, col3 = st.columns(3)

    # --- Practical ---
    with col1:
        st.markdown("### Practical Classes")
        practical_count = st.number_input("No. of practical classes", min_value=0, step=1, value=0, key="p_count")
        practical_hours = st.number_input("Hours", min_value=0, step=1, value=0, key="p_hours")
        practical_minutes = st.number_input("Minutes", min_value=0, max_value=59, step=30, value=0, key="p_mins")
        practical_missed_classes = st.number_input("Missed", min_value=0, step=1, value=0, key="p_missed")

    # --- Tutorial ---
    with col2:
        st.markdown("### Tutorial Classes")
        tutorial_count = st.number_input("No. of tutorial classes", min_value=0, step=1, value=0, key="t_count")
        tutorial_hours = st.number_input("Hours", min_value=0, step=1, value=0, key="t_hours")
        tutorial_minutes = st.number_input("Minutes", min_value=0, max_value=59, step=30, value=0, key="t_mins")
        tutorial_missed_classes = st.number_input("Missed", min_value=0, step=1, value=0, key="t_missed")

    # --- Lecturer ---
    with col3:
        st.markdown("### Lecturer Classes")
        lecturer_count = st.number_input("No. of lecturer classes", min_value=0, step=1, value=0, key="l_count")
        lecturer_hours = st.number_input("Hours", min_value=0, step=1, value=0, key="l_hours")
        lecturer_minutes = st.number_input("Minutes", min_value=0, max_value=59, step=30, value=0, key="l_mins")
        lecturer_missed_classes = st.number_input("Missed", min_value=0, step=1, value=0, key="l_missed")

    # Placeholder for results
    result_placeholder = st.empty()

    # Calculate total class hours
    total_practical = practical_count * time_to_hours(practical_hours, practical_minutes)
    total_tutorial = tutorial_count * time_to_hours(tutorial_hours, tutorial_minutes)
    total_lecturer = lecturer_count * time_to_hours(lecturer_hours, lecturer_minutes)

    total_hours = total_practical + total_tutorial + total_lecturer

    # Calculate total missed hours based on missed classes
    missed_practical_hours = practical_missed_classes * time_to_hours(practical_hours, practical_minutes)
    missed_tutorial_hours = tutorial_missed_classes * time_to_hours(tutorial_hours, tutorial_minutes)
    missed_lecturer_hours = lecturer_missed_classes * time_to_hours(lecturer_hours, lecturer_minutes)

    total_missed_hours = missed_practical_hours + missed_tutorial_hours + missed_lecturer_hours

    # Calculate attendance percentage
    attended_hours = total_hours - total_missed_hours
    attendance_percentage = 0
    if(total_hours != 0):
        attendance_percentage = (attended_hours / total_hours) * 100

    if(attendance_percentage >= 0):
        # Update the result placeholder with formatted output
        result_placeholder.markdown(f"""
            <div style="border: 2px solid #333; padding: 10px; margin-bottom: 20px;">
                <h5 style="color: {'red' if attendance_percentage < 80 else 'green'};">
                    Attendance Percentage: {attendance_percentage:.2f}%
                </h5>
                <h5>Total class hours: {total_hours:.2f} hours</h5>
                <h5>Total missed hours: {total_missed_hours:.2f} hours</h5>
            </div>
        """, unsafe_allow_html=True)

    else:
        result_placeholder.markdown(f"""
            <div style="border: 2px solid #333; padding: 10px; margin-bottom: 20px;">
                <h5 style="color: {'red' if attendance_percentage < 80 else 'green'};">
                    Missed classes too many!
                </h5>
                <h5>Total class hours: 0 hours</h5>
                <h5>Total missed hours: 0 hours</h5>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


