import socket
import tkinter as tk

s = socket.socket()
port = 56789
s.connect(("172.21.5.95", port))

def button_click_action():
    # Define the message to send when the button is clicked
    message = "Change traffic light colors"
    s.send(message.encode())
    response = s.recv(1024)
    print(response.decode())
   
def pedestrianCrossing():
    # Define the message to send when the button is clicked
    message = "You may cross"
    s.send(message.encode())
    response = s.recv(1024)
    print(response.decode())    

def main():
    # Create the GUI window
    root = tk.Tk()
    root.title("Traffic Light Control")

    # Create a button widget
    button = tk.Button(root, text="Change Traffic Light Colors", command=button_click_action)
    button.pack()
   
    #Create a button widget
    button = tk.Button(root, text="You may cross", command=pedestrianCrossing)
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

s.close()