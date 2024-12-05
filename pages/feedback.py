import streamlit as st

st.title("Deixe seu Feedback")

# Criação do formulário de feedback
with st.form(key='feedback_form'):
    nome = st.text_input('Nome:')
    email = st.text_input('E-mail:')
    feedback = st.text_area('Seu Feedback:')
    
 
submit_button = st.form_submit_button(label='Enviar Feedback')

# Ação quando o usuário enviar o feedback
if submit_button:
    if nome and email and feedback:
        st.success(f"Obrigado pelo seu feedback, {nome}!")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Comentário:** {feedback}")
        
        with open('feedbacks.txt', 'a') as file:
            file.write(f"Nome: {nome}\nEmail: {email}\nFeedback: {feedback}\n\n")
        
    else:
        st.error("Por favor, preencha todos os campos antes de enviar.")
