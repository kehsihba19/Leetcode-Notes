import streamlit as st
import pandas as pd 
import streamlit.components.v1 as stc
from data import create_table,add_data,view_data,get_data,update_data,delete,get_id

HTML_BANNER = """
    <div style="background-color:grey;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">LeetCode Notes</h1>
    </div>
    """
def check(a,b):
	if(a=='admin' and b=='admin'):
		return True
	else:
		return False


def main():
	stc.html(HTML_BANNER)
	
	menu=['Main','Admin']
	choice=st.sidebar.selectbox("Menu",menu)

	create_table()

	if choice=='Main':
		
		with st.beta_expander("View All Questions"):
			data = view_data()
			sf = pd.DataFrame(data,columns=["Id","Hint","Link"])
			st.dataframe(sf)

		with st.beta_expander("Get hints of probem"):
			list_of_question = [i[0] for i in view_data()]
			questions = st.selectbox("Select a problem",list_of_question)
			a=get_data(questions)

			if(len(a)):
				id_=a[0][0]
				hint=a[0][1]
				link=a[0][2]
				st.header('Id')
				st.text(str(id_))
				st.header('Hint')
				st.text(hint)
				st.header('Link')
				st.text(link)

	elif choice=='Admin':
		st.subheader("Admin Panel")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')

		if st.sidebar.checkbox("Login"):

			result=check(username,password)

			if result:

				st.success("Logged In as Admin")
				task = st.selectbox("Task",["Read Questions","Add Questions","Update Questions","Delete Questions"])

				if(task=='Read Questions'):

					data = view_data()
					sf = pd.DataFrame(data,columns=["Id","Hint","Link"])
					st.dataframe(sf)

				elif(task=='Add Questions'):

					id_=st.text_input("Id (In Number)")
					link=st.text_input("Link")
					hint=st.text_area("Hint")

					if(st.button("Submit")):

						if(id_=='' or link=='' or hint==''):
							if(id_==''):
								st.warning('Add the id value')
							elif(link==''):
								st.warning('Add the link')
							else:
								st.warning('Add the hint')
						elif(len(get_data(id_))):
							st.warning("Id already exists")
						else:
							add_data(id_,hint,link)
							st.success("Added")
							st.balloons()

				elif(task=='Delete Questions'):
					id_=st.text_input("Id (In Number)")
					if(st.button("Delete Question")):
						if(len(get_data(id_))):
							delete(id_)
							st.success("Deleted Question {}".format(id_))
						else:
							st.warning("Question doesn't exists")

				elif(task=='Update Questions'):
					list_of_question = [i[0] for i in view_data()]
					selected_question = st.selectbox("Question Id",list_of_question)
					question_result=get_data(selected_question)
					if question_result:
						old_id=question_result[0][0]
						old_hint=question_result[0][1]
						old_link=question_result[0][2]
						id_=st.text_input("Id",old_id)
						link=st.text_input("Link",old_link)
						hint=st.text_area("Hint",old_hint)

						if(st.button("Update")):
							if(id_=='' or link=='' or hint==''):
								if(id_==''):
									st.warning('Add the id value')
								elif(link==''):
									st.warning('Add the link')
								else:
									st.warning('Add the hint')
							else:
								update_data(selected_question,id_,hint,link)
								st.success("Updated")
								st.balloons()
			else:
				st.warning("Incorrect Username/Password")

if __name__ == '__main__':
	main()