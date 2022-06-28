import streamlit as st

def function1():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def function2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def function3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function4():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function5():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function6():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function7():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")



func_num = {
    "Function 1": function1,
    "Function 2": function2,
    "Function 3": function3,
    "Function 4": function4,
    "Function 5": function5,
    "Function 6": function6,
    "Function 7": function7
}

selected_func = st.sidebar.selectbox("Select a function!", func_num.keys(),disabled=False)
func_num[selected_func]()