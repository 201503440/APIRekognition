# APIRekognition
Obtener labels de imagen en un Bucket de S3


El request se haria a la siguiente ruta:

http://localhost:5000/getLabels

es un metodo post que recibe un JSON de la siguiente forma:

{ 
    "photo": "ImageName",
    "bucket": "BucketName"
}
