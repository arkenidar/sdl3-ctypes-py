# Note: This is a simple SDL3 example in Python.
# It creates a window and draws a red rectangle on a white background.
# The program uses the SDL3 library to create a window and handle events.
# It initializes the SDL library, creates a window and a renderer, and enters a main loop where it handles events and draws graphics.
# It also handles window events and allows the user to close the window or press the escape key to exit.
# Import necessary modules
import sdl3, ctypes

# Define the main function
# This function will be called when the program is run
@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:

    # Initialize SDL
    # This initializes the SDL library with video and event subsystems
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS ):
        print(f"Failed to initialize library: {sdl3.SDL_GetError().decode()}.")
        return -1

    # Create an SDL window
    # The window is created with a title, width, height, and resizable flag
    # The title is encoded to bytes using UTF-8 encoding
    window = sdl3.SDL_CreateWindow("PySDL3 Example".encode(), 800, 600, sdl3.SDL_WINDOW_RESIZABLE)

    # Create a renderer for the window
    # The renderer is created with the "software" driver
    # This means that the rendering will be done in software rather than using hardware acceleration
    # The renderer is used to draw graphics on the window
    if not (renderer := sdl3.SDL_CreateRenderer(window, "software".encode())):
        print(f"Failed to create renderer: {sdl3.SDL_GetError().decode()}.")
        return -1

    # Main loop flag
    # This flag is used to control the main loop of the program
    running = True

    # Event structure
    # This structure is used to store events that are polled from the event queue
    event = sdl3.SDL_Event()

    while running:
        # Poll events from the event queue
        # This function retrieves events from the event queue and stores them in the event structure
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            match event.type:
                # Handle different types of events
                case sdl3.SDL_EVENT_QUIT:
                    # If the quit event is received, set running to False to exit the loop
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    # If a key is pressed, check if it is the escape key
                    # If it is, set running to False to exit the loop
                    if event.key.key in [sdl3.SDLK_ESCAPE]:
                        running = False

        # Set draw color and clear screen
        rgb_back = (1,1,1)
        # Set the draw color to white (RGB: 1, 1, 1) and alpha: 1.0
        # This color will be used to clear the screen
        sdl3.SDL_SetRenderDrawColorFloat(renderer, *rgb_back, 1.0)
        # Clear the screen with the specified color
        # This function clears the current rendering target with the draw color
        sdl3.SDL_RenderClear(renderer)

        # Set draw color to red and draw a rectangle
        rgb_front = (1,0,0)
        # Set the draw color to red (RGB: 1, 0, 0) and alpha: 1.0
        # This color will be used to draw the rectangle
        sdl3.SDL_SetRenderDrawColorFloat(renderer, *rgb_front, 1.0)
        # Create a rectangle structure
        # This structure defines the position and size of the rectangle
        frect1 = sdl3.SDL_FRect()
        frect1.x = 200.0
        frect1.y = 150.0
        frect1.w = 400.0
        frect1.h = 300.0
        # Draw the rectangle on the screen
        # This function draws a filled rectangle on the current rendering target
        sdl3.SDL_RenderFillRect(renderer, ctypes.byref(frect1))

        # Present the updated renderer
        # This function updates the screen with the rendering performed on the current rendering target
        # It effectively swaps the back buffer with the front buffer, displaying the rendered content
        # to the user
        sdl3.SDL_RenderPresent(renderer)

    # Clean up
    # This function destroys the renderer and window, and quits SDL
    # It is called when the main loop exits
    # This is important to free up resources and avoid memory leaks
    # Destroy the renderer and window
    # This function destroys the renderer and window, and quits SDL
    sdl3.SDL_DestroyRenderer(renderer)
    # Destroy the window
    # This function destroys the window and frees up resources associated with it
    # It is important to call this function to avoid memory leaks
    # It is called when the program exits
    # Destroy the window and quit SDL
    sdl3.SDL_DestroyWindow(window)
    # Quit SDL
    # This function cleans up all initialized subsystems and frees up resources
    sdl3.SDL_Quit()

    # Return 0 to indicate successful execution
    # This is the standard return value for a successful program execution
    # It indicates that the program has completed successfully without errors
    return 0

# Note: This is a simple SDL3 example in Python.
# It creates a window and draws a red rectangle on a white background.
