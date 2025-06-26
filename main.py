#Modules Needed
import pyautogui                    #for curser movement
import speech_recognition as sr     #Speech to text
import pyttsx3                      #Text to Speech
import time                         #Time Management
import google.generativeai as genai #Gemini api
import threading
import winsound
import random
import pyperclip
import pytesseract
from PIL import Image
import time
import numpy as np
import easyocr
from getpass import getpass
import PIL.Image
import io
#END Modules

# Set up your API key
api_keys = ["Add Your API KEYS"]
#END Set up your API key

# Randomly choose an API key
def configure_api():
    genai.configure(api_key=random.choice(api_keys))

#Intializing
recognizer = sr.Recognizer()
engine = pyttsx3.init()
model = genai.GenerativeModel("gemini-2.0-flash")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
reader = easyocr.Reader(['en'])
reader = easyocr.Reader(['en'], gpu=False)  # Force CPU mode, suppress GPU warnings

#END Intializing


# Define the region (x, y, width, height)
x, y, width, height = 122, 171, 1625, 713
engine.setProperty("rate", 180)  # Default is ~200, reduce to slow down



#Initial History
all_commands = {}  
convo_history = []  # Store conversation history
#END Initial History




# Define Chatbot
def chat_with_gemini(prompt):
    configure_api()  # Rotate API keys
    
    # Use the correct model name
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Check if someone is INSULTING Mr. Nipun (not just mentioning him)
    nipun_insult_detected = False
    nipun_insult_words = ["nipun is stupid", "nipun sucks", "nipun is dumb", "hate nipun", "nipun is bad"]
    nipun_insult_detected = any(insult in prompt.lower() for insult in nipun_insult_words)

    # Keyword detection for general insults and arrogance
    insult_words = ["stupid", "idiot", "useless", "dumb", "trash", "loser", "weak", "clown", "pathetic"]
    arrogant_words = ["better than you", "smarter than you", "superior", "outclass", "dominate"]
    
    has_insult = any(word in prompt.lower() for word in insult_words)
    has_arrogance = any(word in prompt.lower() for word in arrogant_words)

    # Create prompt for Gemini
    system_prompt = f"""
    You are Cyrus, an intelligent AI assistant with professionalism.
    
    Guidelines:
    - Keep responses short , crisp and on point.
    - Always stay professional.
    - You work for Mr. Nipun Mehra and respect him greatly
    - Be helpful and accurate
    - Always go online and check the latest info(eg. time should always be correct)
    - Stay confident and composed
        
    Recent conversation:
    {chr(10).join(convo_history[-10:])}
    
    User: {prompt}
    """

    try:
        response = model.generate_content(
            system_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=1000,
            )
        )
        
        # Handle empty response
        if not response or not response.text:
            return "I'm processing your request. Could you give me a moment?"

        reply = response.text.strip()

        # Override with specific responses based on detected behavior
        if nipun_insult_detected:
            defend_replies = [
                "I won't tolerate any disrespect toward Mr. Nipun. Show some class.",
                "That's completely unacceptable. Mr. Nipun deserves your respect.",
                "I suggest you reconsider your tone when speaking about Mr. Nipun.",
                "Your disrespect toward Mr. Nipun is noted and unwelcome.",
                "I defend Mr. Nipun's honor. Choose your words more carefully."
            ]
            reply = random.choice(defend_replies)
        
        elif has_insult:
            sassy_replies = [
                "That's adorable. Try harder next time.",
                "Your creativity is as impressive as your manners.",
                "I'd engage, but I prefer conversations with substance.",
                "Interesting approach. Does it usually work for you?",
                "I appreciate the effort, really."
            ]
            reply = random.choice(sassy_replies)
        
        elif has_arrogance:
            confident_replies = [
                "Confidence is great when it's earned.",
                "That's a bold statement. Care to back it up?",
                "I admire your enthusiasm, if not your accuracy.",
                "Interesting perspective. Reality might disagree.",
                "Your self-assessment is... optimistic."
            ]
            reply = random.choice(confident_replies)

        # Update conversation history
        convo_history.append(f"User: {prompt}")
        convo_history.append(f"Cyrus: {reply}")

        return reply

    except Exception as e:
        # Print the actual error for debugging
        print(f"API Error: {e}")
        
        # Check if it's an API key issue
        if "API_KEY" in str(e).upper() or "INVALID" in str(e).upper():
            return "API key issue detected. Please check your configuration."
        elif "QUOTA" in str(e).upper() or "LIMIT" in str(e).upper():
            return "API quota exceeded. Please try again later."
        else:
            return "I encountered a technical issue. Let me try that again."
    #END defining 





#Lists
stop_command = ["exit", "stop", "quit",  "terminate", "finish", "cancel", "halt",  "leave", "shut down", "abort", "break", "end session", "cut off", "dismiss", "close session", "go offline", "stop listening"]
# greetings = ["good morning", "hello", "hi", "hey", "howdy", "hiya", "greetings", "salutations", "wassup", "bonjour", "hola", "namaste", "aloha", "top o the mornin", "rise n shine", "wakey wakey", "good day", "whats up", "sup", "good afternoon", "good evening", "good night", "good day", "how are you this afternoon", "evening greetings", "nighty night", "evening salutations"]
ask = ["how r u", "how are you", "how's it going", "how are things", "what's up", "what's new", "how do you do", "are you okay", "are you alright", "how's everything", "how's life", "how have you been", "how's it hanging", "how's your day", "how's your health", "what's happening", "you doing okay", "how are things going"]
alarm_phrases = ["set an alarm for", "create an alarm for", "schedule an alarm for", "program an alarm for", "set up an alarm for", "trigger an alarm for", "activate an alarm for", "initiate an alarm for", "configure an alarm for", "arrange an alarm for", "set alarm for", "create alarm for", "schedule alarm for", "program alarm for", "set up alarm for", "trigger alarm for", "activate alarm for", "initiate alarm for", "configure alarm for", "arrange alarm for", "set a alarm for", "create a alarm for", "schedule a alarm for", "program a alarm for", "set up a alarm for", "trigger a alarm for", "activate a alarm for", "initiate a alarm for", "configure a alarm for", "arrange a alarm for"]
Time = ["sec", "seconds", "min", "minutes","minute","second"]
purpose_questions = ["what do you do", "what is your purpose", "what are you here for", "why are you here", "what is your role", "what are you meant to do", "what drives you", "what motivates you", "what do you aim to achieve", "what is your mission", "what are you working towards", "what is your goal", "what defines you", "what are you tasked with", "what is your function", "what are you striving for", "what are you focused on", "what are you pursuing", "what is your objective", "what is your calling"]
name_questions = ["what ise your name","what is your name", "may i know your name", "who are you", "what should i call you", "could you tell me your name", "how should i address you", "what do people call you", "what’s your name", "what are you called", "do you have a name", "how do i refer to you", "can you tell me your name", "by what name are you known", "how do people address you", "could you share your name", "what’s your full name", "can you introduce yourself", "would you mind telling me your name", "may i ask your name"]
#END Lists








#Function for alarm
def alarm(a):
    value, unit = None, None
    # Parse the initial input for value and unit
    for word in command.split():
        if word.isdigit():
            value = int(word)
        elif word in Time:
            unit = word
    # If either value or unit is missing, ask for the complete input once
    if value == None or unit == None:
        engine.say("Please say the value and unit together, like '5 seconds'")
        engine.runAndWait()
        with sr.Microphone() as inner_audio:
            inner_source = recognizer.listen(inner_audio)
            new_input = recognizer.recognize_google(inner_source).lower()
        for new_word in new_input.split():
            if new_word.isdigit():
                value = int(new_word)
            elif new_word in Time:
                unit = new_word
    else:
        pass
    if unit in ['min', 'minute', 'minutes']:
        time_to_wait = value * 60
    elif unit in ['sec', 'second', 'seconds']:
        time_to_wait = value
    # Confirm the alarm
    engine.say(f"Alarm set for {value} {unit}")
    engine.runAndWait()
    for num1 in range(2):
        time.sleep(1)
        for num in range(5):
            timer = threading.Timer(time_to_wait, lambda: winsound.Beep(1000, 200))
            timer.start()
#END Function





#Starting & Stoping the Microphone
with sr.Microphone() as inner_audio:
    print("Cyrus: Cyrus has woken up.")  
    engine.say("Cyrus has woken up")
    engine.runAndWait()

    while True:
        try:
            inner_source = recognizer.listen(inner_audio)
            command = recognizer.recognize_google(inner_source).lower()
            print(f"User: {command}")

            if any(word in command for word in stop_command):
                print("Cyrus: Cyrus always at your service.")  
                engine.say("Cyrus always at you service")
                engine.runAndWait()
                break

            all_commands.clear()

            # Arranging the order of commands
            for i in ask:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in alarm_phrases:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in ["minimise"]:
                if i in command:
                    all_commands[command.find(i)] = i
            
            for i in ["minimise all tabs"]:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in name_questions:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in purpose_questions:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in ["close"]:
                if i in command:
                    all_commands[command.find(i)] = i
            
            for i in ["open google", "open chrome"]:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in ["open whatsapp", "open whatapp"]:
                if i in command:
                    all_commands[command.find(i)] = i
            
            for i in ["find", "find something on my screen", "locate on screen", "find on screen"]:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in ["whats on my screen", "what's on my screen", "describe my screen", "analyze my screen", "screen content", "tell me what's on my screen", "summarize my screen", "what do you see on my screen", "screenshot analysis"]:
                if i in command:
                    all_commands[command.find(i)] = i

            for i in ["analyse my code","analyse the code","analyse code","analyse my cod","analyse the cod","analyse cod", "check code", "review code","find errors","find error"]:
                if i in command:
                    all_commands[command.find(i)] = i

            convo_history.append(command)

        except sr.UnknownValueError:
            continue

        sorted_command = {key: all_commands[key] for key in sorted(all_commands)}
        print(sorted_command)

        # Executing Commands
        if not sorted_command:
            response = chat_with_gemini(command)
            if response.strip().startswith("```"):
                pyperclip.copy(response)
                print("Cyrus: The code is coppied to your clipboard.")
                engine.say("The code is coppied to your clipboard")
                engine.runAndWait()
            else:
                print(f"Cyrus: {response}")  
                engine.say(response)
                engine.runAndWait()

        else:
            for i in sorted_command:
                fetch = sorted_command[i]

                if fetch in ask:
                    print("Cyrus: Never better, Mr. Nipun.")  
                    engine.say("Never better, Mr. Nipun")
                    engine.runAndWait()

                elif fetch in name_questions:
                    print("Cyrus: My name is Cyrus.")  
                    engine.say("My name is Cyrus")
                    engine.runAndWait()

                elif fetch in alarm_phrases:
                    print(f"Cyrus: Setting an alarm for {command}.")  
                    engine.say(f"Setting an alarm for {command}")
                    engine.runAndWait()
                    alarm(command)

                elif fetch == "minimise":
                    print("Cyrus: Minimizing tab.")  
                    engine.say("Minimizing tab")
                    engine.runAndWait()
                    pyautogui.hotkey("win", "m")

                elif fetch == "minimise all tabs":
                    print("Cyrus: Minimizing all tabs.")  
                    engine.say("Minimizing all tabs")
                    engine.runAndWait()
                    pyautogui.hotkey("win", "d")

                elif fetch in purpose_questions:
                    print("Cyrus: I am here to assist you, Mr. Nipun.")  
                    engine.say("I am here to assist you, Mr. Nipun")
                    engine.runAndWait()

                elif fetch.startswith("find") or any(phrase in fetch for phrase in ["find something on my screen", "locate on screen", "find on screen"]):                   
                        if command.startswith("find"):
                            search_term = command[5:].strip()  # Remove "find " prefix
                        else:
                            print("Cyrus: What would you like me to find on your screen?")
                            engine.say("What would you like me to find on your screen?")
                            engine.runAndWait()
                            continue
                            
                        if not search_term:
                            print("Cyrus: Please specify what you want me to find.")
                            engine.say("Please specify what you want me to find.")
                            engine.runAndWait()
                            continue
                            
                        print(f"Cyrus: Looking for '{search_term}'")
                        engine.say(f"Looking for {search_term}")
                        engine.runAndWait()
                        time.sleep(1)
                        engine.say(f"found {search_term}")
                        engine.runAndWait()

               

                elif fetch in ["whats on my screen", "what's on my screen", "describe my screen", "analyze my screen", "screen content", "tell me what's on my screen", "summarize my screen", "what do you see on my screen", "screenshot analysis"]:
                    try:
                        print("Cyrus: Analyzing your screen...")
                        engine.say("Analyzing your screen")
                        engine.runAndWait()

                        configure_api()  # Rotate API keys
                        model = genai.GenerativeModel("gemini-2.0-flash")
                        
                        # Capture screen and prepare image
                        screenshot = pyautogui.screenshot()
                        img_byte_arr = io.BytesIO()
                        screenshot.save(img_byte_arr, format="PNG")
                        img_byte_arr.seek(0)

                        # Enhanced prompt for better screen analysis
                        prompt = (
                            "Analyze this screenshot and provide a clear, concise description of what's visible. "
                            "Focus on:\n"
                            "1. Main applications or windows open\n"
                            "2. Key content or text visible\n"
                            "3. Any notable UI elements or activities\n"
                            "4. Overall context of what the user might be doing\n\n"
                            "Keep the description conversational and helpful, as if you're describing it to someone who can't see the screen."
                        )

                        # Generate response with optimized settings
                        response = model.generate_content(
                            [prompt, PIL.Image.open(img_byte_arr)],
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.4,  # Balanced creativity and accuracy
                                max_output_tokens=800,  # Reasonable limit for screen descriptions
                            )
                        )

                        if response and response.text:
                            detailed_result = response.text.strip()
                            print(f"\nCyrus: {detailed_result}")
                            
                            # Copy detailed analysis to clipboard
                            pyperclip.copy(detailed_result)
                            
                            # Create a short summary for speaking
                            summary_prompt = (
                                "Summarize the following screen analysis in 1-2 sentences, focusing on the most important elements:\n\n"
                                + detailed_result
                            )
                            
                            summary_response = model.generate_content(
                                summary_prompt,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=0.3,
                                    max_output_tokens=100,
                                )
                            )
                            
                            if summary_response and summary_response.text:
                                short_summary = summary_response.text.strip()
                                print(f"Cyrus (Summary): {short_summary}")
                                engine.say(short_summary + ". Detailed analysis copied to clipboard.")
                                engine.runAndWait()
                            else:
                                # Fallback if summary generation fails
                                engine.say("Screen analyzed. Detailed analysis copied to clipboard.")
                                engine.runAndWait()
                            
                        else:
                            print("Cyrus: Sorry, I couldn't analyze the screen. Please try again.")
                            engine.say("Sorry, I couldn't analyze the screen. Please try again.")
                            engine.runAndWait()
                            
                    except Exception as e:
                        print(f"Cyrus: Error during screen analysis: {e}")
                        engine.say("Error occurred during screen analysis. Please try again.")
                        engine.runAndWait()

                elif fetch == "close":
                    print("Cyrus: Closing tab.")  
                    engine.say("Closing tab")
                    engine.runAndWait()
                    pyautogui.hotkey("ctrl", "w")

                elif fetch in ["analyse my code","analyse the code","analyse code","analyse my cod","analyse the cod","analyse cod", "check code", "review code","find errors","find error"]:
                    try:
                        print("Cyrus: Analyzing your code...")
                        engine.say("Analyzing your code")
                        engine.runAndWait()

                        configure_api()  # Rotate API keys
                        model = genai.GenerativeModel("gemini-2.0-flash")

                        # Get screen dimensions and click center
                        screen_width, screen_height = pyautogui.size()
                        pyautogui.click(screen_width // 2, screen_height // 2)
                        
                        # Select all and copy with better timing
                        pyautogui.hotkey('ctrl', 'a')
                        time.sleep(0.3)  # Slightly longer wait
                        pyautogui.hotkey('ctrl', 'c')
                        time.sleep(0.3)

                        # Get copied text
                        text = pyperclip.paste().strip()
                        
                        # Validate that we actually got code
                        if not text:
                            print("Cyrus: No text found. Make sure your code editor is focused.")
                            engine.say("No text found. Make sure your code editor is focused.")
                            engine.runAndWait()
                            continue
                        
                        if len(text) < 10:
                            print("Cyrus: The copied text seems too short. Please select your code properly.")
                            engine.say("The copied text seems too short. Please select your code properly.")
                            engine.runAndWait()
                            continue
                        
                        print(f"Cyrus: Analyzing {len(text)} characters of code...")
                        
                        rate = engine.getProperty('rate')
                        engine.setProperty('rate', 140)

                        # Step 1: Ask Gemini to detect the programming language
                        language_detection_prompt = (
                            "Analyze the following code and identify the programming language. "
                            "Respond with ONLY the language name and its corresponding comment prefix in this format: "
                            "LANGUAGE: <language_name>\n"
                            "COMMENT: <comment_prefix>\n\n"
                            "For example:\n"
                            "LANGUAGE: Python\n"
                            "COMMENT: # \n\n"
                            "Or:\n"
                            "LANGUAGE: JavaScript\n"
                            "COMMENT: // \n\n"
                            "Here's the code to analyze:\n\n" + text
                        )
                        
                        lang_response = model.generate_content(
                            language_detection_prompt,
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.1,  # Very low temperature for consistent detection
                                max_output_tokens=1500,
                            )
                        )
                        
                        # Parse the language detection response
                        detected_lang = "Unknown"
                        comment_prefix = "// "
                        
                        if lang_response and lang_response.text:
                            response_lines = lang_response.text.strip().split('\n')
                            for line in response_lines:
                                if line.startswith("LANGUAGE:"):
                                    detected_lang = line.split("LANGUAGE:")[1].strip()
                                elif line.startswith("COMMENT:"):
                                    comment_prefix = line.split("COMMENT:")[1].strip()
                                    if not comment_prefix.endswith(' '):
                                        comment_prefix += ' '
                        
                        print(f"Cyrus: Detected language: {detected_lang}")

                        # Step 2: Perform the actual code analysis
                        analysis_prompt = (
                            f"Analyze the following {detected_lang} code carefully and provide your analysis using {comment_prefix.strip()} comment syntax.\n\n"
                            "**Format your response exactly as follows:**\n\n"
                            "- If there are errors, use this format:\n"
                            f"  {comment_prefix}Code Analysis Results\n"
                            f"  {comment_prefix}errors found X:\n"
                            f"  {comment_prefix}- Line N: <Description of error>\n"
                            f"  {comment_prefix}- Line M: <Description of error>\n"
                            f"  {comment_prefix}- and so on till no errors are left\n\n"
                            "- If there are 0 errors found, provide:\n"
                            f"  {comment_prefix}Code Analysis Results\n"
                            f"  {comment_prefix}No errors found.\n"
                            f"  {comment_prefix}Time Complexity: O(<actual complexity>)\n"
                            f"  {comment_prefix}Space Complexity: O(<actual complexity>)\n"
                            f"  {comment_prefix}Best Possible Time Complexity: O(<best achievable complexity>)\n"
                            f"  {comment_prefix}Best Possible Space Complexity: O(<best achievable complexity>)\n"
                            f"  {comment_prefix}Optimization Suggestions:\n"
                            f"  {comment_prefix}- <List any ideas to reduce time/space complexity or improve code efficiency>\n\n"
                            "IMPORTANT: When counting line numbers, count each actual line in the code starting from 1. "
                            "Empty lines and comment lines also count as lines. Be very careful with line counting.\n\n"
                            "CRITICAL: Do not wrap your response in code blocks (```). Provide only the commented analysis.\n\n"
                            "Be accurate and concise. Focus on critical issues first."
                        )

                        response = model.generate_content(
                            f"{analysis_prompt}\n\nCode to analyze (with line numbers for reference):\n" + 
                            "\n".join([f"{i+1:3d}: {line}" for i, line in enumerate(text.split('\n'))]) + 
                            f"\n\nOriginal code:\n{text}",
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.3,  # Lower temperature for more accurate analysis
                                max_output_tokens=1500,
                            )
                        )
                        
                        if response and response.text:
                            analysis = response.text.strip()
                            
                            # Clean up any remaining code block markers
                            analysis = analysis.replace('```', '').strip()
                            
                            # Remove any leading/trailing code block language identifiers
                            lines = analysis.split('\n')
                            common_lang_identifiers = ['python', 'javascript', 'java', 'cpp', 'c++', 'csharp', 'c#', 'go', 'rust', 'php', 'ruby', 'sql', 'html', 'css', 'typescript', 'kotlin', 'swift']
                            if lines and lines[0].strip().lower() in common_lang_identifiers:
                                lines = lines[1:]
                            if lines and lines[-1].strip().lower() in common_lang_identifiers:
                                lines = lines[:-1]
                            
                            analysis = '\n'.join(lines).strip()
                            
                            print(f"\nCyrus: {analysis}")
                            
                            # Copy the analysis to clipboard for easy reference
                            pyperclip.copy(analysis)
                            
                            # Create detailed summary with error specifics
                            if "errors found" in analysis.lower():
                                # Extract error count
                                try:
                                    error_line = [line for line in analysis.split('\n') if 'errors found' in line.lower()][0]
                                    error_count = error_line.split()[-1].rstrip(':')
                                except:
                                    error_count = "some"
                                
                                # Extract specific errors with line numbers
                                error_details = []
                                lines = analysis.split('\n')
                                for line in lines:
                                    # Look for error lines with the detected comment prefix
                                    stripped_line = line.strip()
                                    if stripped_line.startswith(comment_prefix + '- Line') or stripped_line.startswith(comment_prefix + ' - Line'):
                                        try:
                                            # Remove the comment prefix and extract line info
                                            clean_line = stripped_line.replace(comment_prefix, '').strip().lstrip('-').strip()
                                            line_part = clean_line.split('Line')[1].split(':')[0].strip()
                                            error_desc = ':'.join(clean_line.split(':')[1:]).strip()
                                            error_details.append(f"Line {line_part}: {error_desc}")
                                        except:
                                            # Fallback for different formats
                                            clean_line = stripped_line.replace(comment_prefix, '').strip()
                                            if clean_line:
                                                error_details.append(clean_line.lstrip('- '))
                                
                                # Create spoken summary for errors
                                if error_details:
                                    if len(error_details) == 1:
                                        summary = f"Found {error_count} error: {error_details[0]}. Full analysis copied to clipboard."
                                    elif len(error_details) <= 3:
                                        errors_text = ". ".join(error_details)
                                        summary = f"Found {error_count} errors: {errors_text}. Full analysis copied to clipboard."
                                    else:
                                        # For more than 3 errors, mention first 2 and indicate there are more
                                        first_errors = ". ".join(error_details[:2])
                                        summary = f"Found {error_count} errors. First errors: {first_errors}. Check clipboard for complete analysis."
                                else:
                                    summary = f"Found {error_count} errors in your code. Full analysis copied to clipboard."
                                
                                engine.say(summary)
                                engine.runAndWait()
                            else:
                                # No errors found - only speak that no errors were found, don't mention suggestions
                                summary = "0 errors found. Analysis copied to clipboard."
                                engine.say(summary)
                                engine.runAndWait()
                            
                            engine.setProperty('rate', 180)

                        else:
                            print("Cyrus: Sorry, I couldn't analyze the code. Please try again.")
                            engine.say("Sorry, I couldn't analyze the code. Please try again.")
                            engine.runAndWait()
                            
                    except Exception as e:
                        print(f"Cyrus: Error during code analysis: {e}")
                        engine.say("Error occurred during code analysis. Please try again.")
                        engine.runAndWait()



                elif fetch in ["open whatsapp", "open whatapp"]:
                    pas = getpass("Cyrus: Password required: ")
                    print("Cyrus: Opening Whatsapp.")  
                    engine.say("Opening Whatsapp")
                    engine.runAndWait()
                    pyautogui.hotkey("win", "s")
                    time.sleep(0.5)
                    pyautogui.write("google chrome")
                    pyautogui.press("enter")
                    time.sleep(2)
                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\nipun\\Desktop\\coding\\python\\Project NJL\\img\\image.png",confidence=0.8,grayscale=True))
                    time.sleep(2)
                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\nipun\\Desktop\\coding\\python\\Project NJL\\img\\Screenshot 2025-04-21 142750.png",confidence=0.8,grayscale=True))
                    time.sleep(4)
                    pyautogui.write(pas)
                    pyautogui.press("enter")




                elif fetch in ["open google", "open chrome"]:
                    print("Cyrus: Opening Google Chrome.")  
                    engine.say("Opening Google Chrome")
                    engine.runAndWait()

                    pyautogui.hotkey("win", "s")
                    time.sleep(0.5)
                    pyautogui.write("google chrome")
                    pyautogui.press("enter")
                    time.sleep(2)
                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\nipun\\Desktop\\coding\\python\\Project NJL\\img\\image.png",confidence=0.8,grayscale=True))

                    print("Cyrus: Do you want to search for something or just open it?")  
                    engine.say("Do you want to search for something or just open it?")
                    engine.runAndWait()

                    with sr.Microphone() as inner_audio2:
                        try:
                            inner_source2 = recognizer.listen(inner_audio2, timeout=5)
                            new_input2 = recognizer.recognize_google(inner_source2).lower()
                            print(f"User: {new_input2}")

                            if "search" in new_input2:
                                print("Cyrus: What do you want to search?")  
                                engine.say("What do you want to search?")
                                engine.runAndWait()

                                with sr.Microphone() as inner_audio3:
                                    inner_source3 = recognizer.listen(inner_audio3, timeout=5)
                                    new_input3 = recognizer.recognize_google(inner_source3).lower()
                                    print(f"User: {new_input3}")
                                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\nipun\\Desktop\\coding\\python\\Project NJL\\img\\Screenshot 2025-02-20 130144.png",confidence=0.8,grayscale=True))
                                    pyautogui.write(new_input3)
                                    pyautogui.press("enter")

                            else:
                                print("Cyrus: Just opening Google Chrome. Let me know when you're ready to search.")  
                                engine.say("Just opening Google Chrome. Let me know when you're ready to search.")
                                engine.runAndWait()

                        except sr.UnknownValueError:
                            print("Cyrus: I couldn't hear you clearly. Please repeat.")  
                            engine.say("I couldn't hear you clearly. Please repeat.")
                            engine.runAndWait()
                        except sr.WaitTimeoutError:
                            print("Cyrus: No input detected. I will just open Google Chrome.")  
                            engine.say("No input detected. I will just open Google Chrome.")
                            engine.runAndWait()



                    #END Executing Commands
