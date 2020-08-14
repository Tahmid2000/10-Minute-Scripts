# 10 Minute Scripts
Some short scripts I wrote to make my life easier. Feel free to use and optimize them for your needs!

## Automated File Transfer (utd_files.py)
<strong>Use:</strong> I personally use this for my UTD class files. 
I have my UTD directory set up with leaf directories of each of the courses I'm currently taking. 
Previously, whenever I downloaded a file for a specfic class,
I would have to name it with that course's 4 digit ID and then isnert it into the designated folder.
With this script, all I have to do is rename the file with the 4 digit ID and the file automatically
moves into the designated folder. Using cron jobs, I have this script running once a minute to check
if there are any files that need transferring. <br><br>
<strong>Set Up Cron Job:</strong><br>
1. $ crontab -e 
   * If this doesn't work type "VISUAL=nano crontab -e" instead
2. Add this cron job, with your appropriate path
   * "* * * * * /usr/bin/python3 "/path/to/script" "
3. Save the file and you're done!
## Search Google, Youtube, Amazon (search_script.py)
<strong>Use:</strong> Search Google, Youtube, Amazon with with a simple terminal command and save
many minutes of your life by eliminating many steps in between. <br><br>
<strong>Set Up:</strong><br>
I used this <a href="https://dbader.org/blog/how-to-make-command-line-commands-with-python">site</a>. Here is a short summary:
1. cd to the directory with the script, then:
   * $ chmod +x search_script.py
2. Make sure the "#!/usr/bin/env python3" is the first line of the script!
3. In the same directory:
   * $ mv search_script.py search
     * It does not have to be search, it can be whatever command you want like "lookup"
4. Create a 'bin' directory in your home directory with:
   * $ mkdir -p ~/bin
5. Then cp the command to this directory with:
   * $ cp search ~/bin
6. Open your bash profile with:
   * $ open ~/.bash_profile
7. Add the following line to your bash_profile:
   * export PATH=$PATH":$HOME/bin
8. Save the file and you're done! 

<strong>How to use the commands:</strong>
* $ search django docs
  * Googles 'django docs'
* $ search
  * Googles whatever is on your clipboard (really useful for copying a coding error and searching it up)
* $ search yt React JS for beginners
  * Searches Youtube for 'React JS for beginners'
* $ search am monitor
  * Searches Amazon for 'monitor'
