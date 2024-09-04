
from pytube import YouTube

# youtube_downloader.py

class YouTubeDownloader:
    
    
    @staticmethod
    def download_video(video_url, output_path='video.mp4'):
        
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download(filename=output_path)
            return output_path
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            raise e
        

class gerado_whatsapp:
    def __init__(self):
        self.empresa = 'MetaInnovate'
        self.mensagem_link_gerado = 'Seu link foi gerado com sucesso!'
        self.sobre= f"Sobre o {self.empresa}"
        self.textoSobre = f"O {self.empresa} nasceu da ideia de combinar inovação tecnológica com simplicidade, criando uma plataforma que coloca o poder da conversão e da inteligência artificial ao alcance de todos. Desenvolvemos soluções que facilitam o dia a dia digital, permitindo que você transforme vídeos, imagens, e links de maneira eficiente e sem complicações. Nossa missão é oferecer ferramentas que não apenas acompanhem as necessidades tecnológicas atuais, mas que também antecipem as demandas futuras. No MetaCogni, cada recurso é projetado com foco na usabilidade e na eficácia, utilizando tecnologias de ponta para garantir que você tenha sempre as melhores soluções ao seu dispor. Com uma equipe dedicada de especialistas em tecnologia e IA, estamos comprometidos em fornecer uma experiência digital robusta e intuitiva. Queremos que o MetaCogni seja o seu parceiro de confiança na jornada digital, ajudando você a explorar novas possibilidades e alcançar resultados excepcionais."
        self.avisgerador = "Ao preencher o formulário, concordo * em receber comunicações de acordo com meus interesses, pode cancelar a qualquer momento."
        self.menu = ""
        self.avisgerador = "Ao preencher o formulário, concordo * em receber comunicações de acordo com meus interesses, pode cancelar a qualquer momento."


        # Adicione mais textos conforme necessário

    def get_textos(self):
        return {
            'nomeSite': self.empresa,
            'mensagemlinkgerado': self.mensagem_link_gerado,
            "sobre": self.sobre,
            "avisgerador": self.avisgerador,
            "textosobre": self.textoSobre,
            "menu": self.menu,
            "avisgerador": self.avisgerador
            
        }