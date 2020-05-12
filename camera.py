import cv2 
class Videocamera:
    '''
    Class responsible for connecting to the IP-camera
    '''
    def __init__(self, ID, url, container):
        '''
        Inicialize the IP-camera object and configures camera parameters
        Parameters:
            -ID - unique name of camera
            -url - IP adress of camera if url = 0 - will be used the web-camera
            -container - container for frame
        '''
        self.id = ID
        self.cont = container
        self.cap = cv2.VideoCapture(url)
        self.cap.set(cv2.CAP_PROP_FPS, 24) # Чистота кадров
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.
    def get_frame(self):
        '''
        Gets one frame from the video and packs it into a container        
        '''
        for i in range(2): #разогрев камеры
            self.cap.read()
        self.ret, self.frame = self.cap.read()
        try:
            self.cont.put_nowait(self.frame)
        except:
            return None
    def im_frame(self, name_window):
        '''   
        Displays one frame per screen 
        If frame is not exist - stop the work of camera
        Parametets:
            name_window - name of the display window
        '''
        try:
            cv2.imshow(name_window, self.get_frame())
        except:
            print('The frame is not received')
            self.stop()
    def stop(self):
        '''
        Interrupts the connection to the camera
        '''
        self.cap.release()
        