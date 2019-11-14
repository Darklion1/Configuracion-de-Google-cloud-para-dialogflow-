import logging
import dialogflow
from flask import Flask, render_template, request, redirect, url_for

def delete_intent(project_id, intent_id):
   ##eliminar el intentito del chabot con python
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(intent_path)
    print('la intencion se ha eliminado')

def create_intent(project_id, display_name, training_phrases_parts,message_texts):
    
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)
    ##aux=intents_client.get_token(parent,intent)
    print('Intent created: {}'.format(response))

app = Flask(__name__)

@app.route('/')
def template():
    return render_template('form.html')

@app.route('/elimina')
def elimina():
    return render_template('index.html')

@app.route('/eliminar',methods=['GET'])
def eliminar():
    iselva=request.args.get('eli')
    delete_intent('pruebafinal-255517',iselva)
    return ('el intento esta eliminado ')

@app.route('/usuario',methods=['GET'])
def usuario():


 nombreUser = request.args.get('nombreUser')
 
 p1=request.args.get('p1')
 p2=request.args.get('p2')
 p3=request.args.get('p3')
 p4=request.args.get('p4')

 res=request.args.get('respuesta1')
 res2=request.args.get('respuesta2')

 datos=[p1,p2,p3,p4]
 respuestas=[res,res2]


 create_intent('pruebafinal-255517',nombreUser,datos,respuestas)
 print(""+nombreUser)
 return "<h1>Nombre Del Intento es    " + nombreUser +"</h1>"+"<h2>las preguntas son</h2>"+p1+"<br>"+p2+"<br>"+p3+"<br>"+p4+"<h2>Las presuestas son</h2>"+res+"<br>"+res2


if __name__== '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
