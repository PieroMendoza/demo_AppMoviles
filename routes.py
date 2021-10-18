from flask import Blueprint, request, send_from_directory
import os

api_images = Blueprint('api_images', __name__)

@api_images.route("/upload", methods=['POST'])
def upload_image():
    if request.method == "POST":
        file = request.files['file']
        try:
            file.save(os.getcwd() + "/images/" + file.filename)
            return "Imagen guardada"
        except FileNotFoundError:
            return "Folder no existe"
        

@api_images.route('/image/<string:filename>')
def get_image(filename):
    return send_from_directory(os.getcwd() + "/images/", path=filename, as_attachment=False)



@api_images.route('/download/image/<string:filename>')
def download_image(filename):
    return send_from_directory(os.getcwd() + "/images/", path=filename, as_attachment=True)
  

@api_images.route('/delete', methods=['POST'])
def remove_image():
    filename = request.form['filename']

    #VERIFICAMOS SI ES UN FICHERO
    if os.path.isfile(os.getcwd() + "/images/" + filename) == False:
        return "Esto no es un archivo"
    else:
        try:
            os.remove(os.getcwd() + "/images/" + filename)
        except OSError:
            return "No se elimino el archivo"
        return "Imagen eliminada"
