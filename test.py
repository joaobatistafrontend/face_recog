import  face_recognition
import  os , sys
import  cv2


#Ajudante
def  face_confiança(face_distance , face_match_threshold =0.6):
    intervalo  = ( 1.0  -  face_match_threshold )
    valor_linear  = ( 1,0  -  face_distance ) / ( intervalo  *  2,0 )

    if face_distance  >  face_match_threshold :
        return  str ( round ( valor_linear *  100 , 2 )) +  '%'
    else:
        valor  = ( valor_linear  + (( 1,0  -  valor_linear ) *  math.pow (( valor_linear  -  0,5 ) *  2 , 0,2 ))) *  100
        return  str ( round ( valor , 2 )) +  '%'


class  Reconhecimentofacial:
    face_locations  = []
    face_encodings  = []
    face_names  = []
    known_face_encodings  = []
    nomes_faces_conhecidos  = []
    process_current_frame  = True

    def  __init__ ( self ):
        self. encode_faces ()

    def  encode_faces ( self ):
        for  imagem  in  os . listdir ( 'img' ):
            face_image  =  face_recognition . load_image_file ( f"img/{ imagem } " )
            codificação_face  =  face_recognition. face_encodings ( face_image )[ 0 ]

            self. known_face_encodings . anexar ( codificação_face)
            self. nomes_face_conhecidos . anexar ( imagem )
        print ( self . known_face_names )



Reconhecimentofacial()