import smtplib
import time
import os
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Color codes for stylish output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class WorkingNotificationSystem:
    def __init__(self):
        # Your Gmail configuration
        self.sender_email = "you260411@gmail.com"
        self.app_password = "dpvd khof ttfo byod"
        self.receiver_email = None
        self.sent_count = 0
        self.total_to_send = 0
        self.message_content = ""
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_logo(self):
        """Print awesome ASCII logo with colors - CENTERED"""
        logo = f"""
{Colors.CYAN}
    ╔══════════════════════════════════════════╗
    ║                EMAIL BOMBER🥷🏼          ║
    ║                BY ANISH-AXE🎩            ║
    ╚══════════════════════════════════════════╝
    
   _____                 
  /  _  \ ___  ___ ____  
 /  /_\  \\  \/  // __ \ 
/    |    \>    <\  ___/ 
\____|__  /__/\_ \\___  >
        \/      \/    \/ 
   
   WhatsApp : +977 9806167776
   GitHub : Anish-Axe
   Owner : Anish 
{Colors.END}
"""
        print(logo)
        
    def print_header(self):
        """Print stylish header with logo"""
        self.clear_screen()
        self.print_logo()
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.PURPLE}           🚀 ADVANCED NOTIFICATION SYSTEM{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        print(f"{Colors.YELLOW}STATUS🗝️: {Colors.GREEN} ACTIVE ✅{Colors.END}")
        print(f"{Colors.YELLOW}TOOL🔫: {Colors.GREEN} FREE 🔥{Colors.END}")
        print(f"{Colors.CYAN}{'-'*60}{Colors.END}")
        
    def print_success(self, message):
        """Print success message"""
        print(f"{Colors.GREEN}🎯 {message}{Colors.END}")
        
    def print_error(self, message):
        """Print error message"""
        print(f"{Colors.RED}💥 {message}{Colors.END}")
        
    def print_warning(self, message):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")
        
    def print_info(self, message):
        """Print info message"""
        print(f"{Colors.BLUE}🔹 {message}{Colors.END}")
        
    def print_progress(self, message):
        """Print progress message"""
        print(f"{Colors.CYAN}🚀 {message}{Colors.END}")
        
    def open_facebook(self):
        """Open Facebook contact"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.BLUE}📱 CONTACT ME ON FACEBOOK{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        print(f"{Colors.WHITE}🔗 Facebook Profile:{Colors.END}")
        print(f"{Colors.CYAN}   https://facebook.com/anish.pariyar{Colors.END}")
        print(f"\n{Colors.YELLOW}📢 Opening Facebook in your browser...{Colors.END}")
        
        # Open Facebook profile
        facebook_url = "https://www.facebook.com/anish.pariyar.71868"
        webbrowser.open(facebook_url)
        
        print(f"\n{Colors.GREEN}✅ FACEBOOK PROFILE OPENED!{Colors.END}")
        print(f"{Colors.WHITE}💬 FEEL FREE TO MESSAGE ME ON FACEBOOK!{Colors.END}")
        print(f"{Colors.CYAN}{'-'*50}{Colors.END}")
        input(f"{Colors.WHITE}Press Enter to continue...{Colors.END}")
    
    def show_how_to_use(self):
        """Show how to use the tool"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}📖 HOW TO USE THIS TOOL{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        print(f"{Colors.WHITE}{Colors.BOLD}🎯 STEP-BY-STEP GUIDE:{Colors.END}")
        print(f"{Colors.CYAN}1. {Colors.WHITE}FIRST, TEST GMAIL CONNECTION (Option 1⚡){Colors.END}")
        print(f"{Colors.CYAN}2. {Colors.WHITE}ENTER TARGET EMAIL ADDRESS (Option 2⚡){Colors.END}")
        print(f"{Colors.CYAN}3. {Colors.WHITE}START SENDING MESSAGES (Option 3⚡){Colors.END}")
        print(f"{Colors.CYAN}4. {Colors.WHITE}MONITOR PROGRESS IN DASHBOARD (Option 4⚡){Colors.END}")
        
   
        
        
        print(f"\n{Colors.BLUE}{Colors.BOLD}📞 NEED HELP?{Colors.END}")
        print(f"{Colors.WHITE}• Contact via Facebook (Option 5){Colors.END}")
        print(f"{Colors.WHITE}• WhatsApp: +977 9806167776{Colors.END}")
        print(f"{Colors.WHITE}• GitHub: Anish-Axe{Colors.END}")
        
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        input(f"{Colors.WHITE}Press Enter to continue...{Colors.END}")
    
    def setup_recipient(self):
        """Setup recipient information"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}👤 RECIPIENT SETUP{Colors.END}")
        print(f"{Colors.CYAN}{'='*40}{Colors.END}")
        
        self.receiver_email = input(f"{Colors.WHITE}🎯 ENTER TARGET EMAIL ADDRESS: {Colors.END}").strip()
        
        if not self.receiver_email:
            self.print_error("No email entered!")
            time.sleep(2)
            return False
            
        # Verify this is intentional
        print(f"\n{Colors.YELLOW}⚠️  TARGET ACQUIRED: {Colors.WHITE}{self.receiver_email}{Colors.END}")
        confirm = input(f"{Colors.WHITE}🎯 CONFIRM LAUNCH? (yes/no): {Colors.END}").strip().lower()
        
        if confirm == 'yes':
            self.print_success("TARGET LOCKED! RECIPIENT SETUP COMPLETE!")
            time.sleep(2)
            return True
        else:
            self.print_error("Mission aborted. Operation cancelled.")
            time.sleep(2)
            return False
    
    def send_real_email(self):
        """Send one ACTUAL email using your app password"""
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            msg['Subject'] = f"🚀 Notification #{self.sent_count + 1} - AXE "
            
            # Email body - COOL DESIGN
            body = f"""
╔══════════════════════════════════════════╗
║              🚀 NOTIFICATION             ║
║              ✨ BY AXE.                         ║
╚══════════════════════════════════════════╝

📧 Message #{self.sent_count + 1} of {self.total_to_send}
⏰ Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

💬 Content:
{self.message_content}

────────────────────────────────────────────
👤 Owner: Axe
🔗 GitHub: Anish-Axe

 I’m that bloody f**king program — AXE 🪓. Remember the name.
────────────────────────────────────────────

"Code is like humor. When you have to explain it, it's bad." - Axe
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to Gmail and send ACTUAL email
            self.print_progress("Establishing secure connection to Gmail...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            
            # Login with app password
            clean_password = self.app_password.replace(" ", "")
            server.login(self.sender_email, clean_password)
            
            # Send the actual email
            text = msg.as_string()
            server.sendmail(self.sender_email, self.receiver_email, text)
            server.quit()
            
            self.sent_count += 1
            self.print_success(f"MESSAGE #{self.sent_count} DELIVERED SUCCESSFULLY!")
            print(f"{Colors.WHITE}   🎯 TARGET: {self.receiver_email}{Colors.END}")
            print(f"{Colors.WHITE}   ⏰ TIME: {datetime.now().strftime('%H:%M:%S')}{Colors.END}")
            print(f"{Colors.WHITE}   📊 PROGRESS: {self.sent_count}/{self.total_to_send}{Colors.END}")
            
            # Check if all emails sent
            if self.sent_count >= self.total_to_send:
                print(f"\n{Colors.GREEN}🎉 MISSION ACCOMPLISHED! All {self.total_to_send} emails deployed!{Colors.END}")
                return False
            return True
            
        except Exception as e:
            self.print_error(f"LAUNCH FAILED: {str(e)}")
            return False
    
    def start_scheduled_emails(self):
        """Start sending scheduled emails every 2 seconds"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}🚀 LAUNCH SEQUENCE INITIATED{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        # Check if recipient is set
        if not self.receiver_email:
            self.print_error("NO TARGET ACQUIRED! PLEASE SET RECIPIENT EMAIL FIRST!")
            time.sleep(3)
            return
        
        # Get sending details
        try:
            self.total_to_send = int(input(f"{Colors.WHITE}🎯 ENTER TOTAL NUMBER OF MESSAGES TO LAUNCH: {Colors.END}"))
            self.message_content = input(f"{Colors.WHITE}💬 ENTER YOUR MESSAGE CONTENT: {Colors.END}")
            
            if self.total_to_send <= 0:
                self.print_error("Please enter a positive number!")
                time.sleep(2)
                return
                
        except ValueError:
            self.print_error("Please enter a valid number!")
            time.sleep(2)
            return
        
        # Show configuration
        print(f"\n{Colors.BOLD}{Colors.PURPLE}⚙️  MISSION PARAMETERS:{Colors.END}")
        print(f"{Colors.WHITE}   🚀 LAUNCHER: {self.sender_email}{Colors.END}")
        print(f"{Colors.WHITE}   🎯 TARGET: {self.receiver_email}{Colors.END}")
        print(f"{Colors.WHITE}   📦 PAYLOAD: {self.total_to_send} messages{Colors.END}")
        print(f"{Colors.WHITE}   ⚡ INTERVAL: {Colors.CYAN}Every 2 seconds{Colors.END}")
        print(f"{Colors.WHITE}   💬 CONTENT: {self.message_content}{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        # Final confirmation
        confirm = input(f"{Colors.YELLOW}🚀 INITIATE LAUNCH SEQUENCE? (yes/no): {Colors.END}").strip().lower()
        if confirm != 'yes':
            self.print_error("Launch sequence aborted by user.")
            time.sleep(2)
            return
        
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}🎯 LAUNCH IN PROGRESS{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        # Send first email immediately
        self.print_progress("LAUNCHING FIRST MESSAGE NOW...")
        success = self.send_real_email()
        
        if not success:
            self.print_error("Critical failure on first launch. Mission terminated.")
            time.sleep(3)
            return
        
        # Send remaining emails with 2-second intervals
        email_count = 1  # First email already sent
        
        try:
            while email_count < self.total_to_send:
                print(f"\n{Colors.CYAN}⏰ PREPARING NEXT LAUNCH IN 2 SECONDS (#{email_count + 1})...{Colors.END}")
                
                # Wait 2 seconds with countdown
                for second in range(2, 0, -1):
                    print(f"{Colors.YELLOW}   NEXT LAUNCH IN {second} SECONDS...{Colors.END}", end='\r')
                    time.sleep(1)
                
                print(" " * 50, end='\r')  # Clear line
                
                # Send next email
                self.print_progress(f"Launching message #{email_count + 1}...")
                if self.send_real_email():
                    email_count += 1
                else:
                    self.print_error("Mission critical failure. Launch sequence terminated.")
                    break
                
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🛑 LAUNCH SEQUENCE INTERRUPTED{Colors.END}")
            print(f"{Colors.WHITE}📊 MISSION REPORT: {self.sent_count}/{self.total_to_send} messages deployed{Colors.END}")
        
        input(f"\n{Colors.WHITE}PRESS ENTER TO RETURN TO COMMAND CENTER...{Colors.END}")
    
    def test_connection(self):
        """Test if Gmail connection works"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}🧪 SYSTEM DIAGNOSTICS{Colors.END}")
        print(f"{Colors.CYAN}{'='*40}{Colors.END}")
        
        try:
            clean_password = self.app_password.replace(" ", "")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, clean_password)
            server.quit()
            self.print_success("SYSTEM STATUS: OPTIMAL")
            self.print_success("Gmail connection: STABLE")
            self.print_success("Launch systems: READY")
            time.sleep(3)
            return True
        except Exception as e:
            self.print_error(f"SYSTEM FAILURE: {e}")
            time.sleep(3)
            return False
    
    def show_status(self):
        """Show current status"""
        self.print_header()
        print(f"{Colors.BOLD}{Colors.PURPLE}📊 MISSION CONTROL DASHBOARD{Colors.END}")
        print(f"{Colors.CYAN}{'='*40}{Colors.END}")
        print(f"{Colors.WHITE}🚀 LAUNCHER: {self.sender_email}{Colors.END}")
        print(f"{Colors.WHITE}🎯 TARGET: {self.receiver_email or 'Not acquired'}{Colors.END}")
        print(f"{Colors.WHITE}📨 MESSAGES DEPLOYED: {self.sent_count}{Colors.END}")
        print(f"{Colors.WHITE}👤 COMMANDER: ANISH {Colors.END}")
        print(f"{Colors.WHITE}🔗 GITHUB: ANISH-AXE{Colors.END}")
        print(f"{Colors.CYAN}{'-'*40}{Colors.END}")
        input(f"{Colors.WHITE}Press Enter to continue...{Colors.END}")
    
    def menu(self):
        """Main menu"""
        while True:
            self.print_header()
            print(f"{Colors.BOLD}{Colors.PURPLE}🎮 COMMAND CENTER{Colors.END}")
            print(f"{Colors.CYAN}{'='*50}{Colors.END}")
            print(f"{Colors.WHITE}1. {Colors.CYAN} SYSTEM CHECK🧾{Colors.END}")
            print(f"{Colors.WHITE}2. {Colors.CYAN} ENTER GMAIL🎯{Colors.END}")
            print(f"{Colors.WHITE}3. {Colors.CYAN} HOW MUCH🚀{Colors.YELLOW}(EVERY 2 SECONDS){Colors.END}")
            print(f"{Colors.WHITE}4. {Colors.CYAN} MISSION DASHBOARD📊{Colors.END}")
            print(f"{Colors.WHITE}5. {Colors.CYAN} CONTACT FACEBOOK📱{Colors.END}")
            print(f"{Colors.WHITE}6. {Colors.CYAN} HOW TO USE📖{Colors.END}")
            print(f"{Colors.WHITE}7. {Colors.RED} EXIT COMMAND CENTER📍{Colors.END}")
            print(f"{Colors.CYAN}{'-'*50}{Colors.END}")
            
            choice = input(f"{Colors.WHITE}🎯 SELECT OPERATION (1-7): {Colors.END}").strip()
            
            if choice == '1':
                self.test_connection()
            elif choice == '2':
                self.setup_recipient()
            elif choice == '3':
                self.start_scheduled_emails()
            elif choice == '4':
                self.show_status()
            elif choice == '5':
                self.open_facebook()
            elif choice == '6':
                self.show_how_to_use()
            elif choice == '7':
                self.print_header()
                print(f"{Colors.GREEN}👋 MISSION CONTROL SIGNING OFF!{Colors.END}")
                print(f"{Colors.CYAN}{'='*50}{Colors.END}")
                break
            else:
                self.print_error("INVALID COMMAND! PLEASE SELECT 1-7")
                time.sleep(2)

# 🚀 START THE PROGRAM
if __name__ == "__main__":
    system = WorkingNotificationSystem()
    system.menu()