# **Spotify Playlist Printout Generator**

Jordan Kahn (jskahn2) | Moderator: Brian Huang (brianbh2)

## **Abstract**

### **Description:**

This mobile/web application allows users to turn their Spotify playlists or albums into paper printouts that they can share with others. The printouts will contain the playlist/album cover photo, the names and artists of the first ~15 songs on the playlist, and a scannable QR code that links directly to the playlist or album on Spotify.

### **Project Motivation:**

The purpose of this project is to provide a tangible way for people to interact with their Spotify playlists and albums. I’ve noticed that the main way people share music with each other is by sending links to streaming services. I feel like this practice could become even more meaningful if done in the physical world. With this tool, one could make printouts of a playlist they made for a friend or a significant other as part of a gift. On the other hand, music artists could use this tool to print out “hard copies” of their albums and give them away to potential fans at a low cost (compared to burning CDs).

## **Technical Specification**

- Platform: Cross-platform app (React Native)
- Programming Languages: JavaScript (front end) and Python (backend and Flask)
- Stylistic Conventions: Airbnb JavaScript Style Guide, Jest testing
- API: Spotify API
- IDE: Visual Studio Code
- Tools/Interfaces: Mobile devices and Web Browsers
- Target Audience: Music lovers and small/independent music artists/bands

## **Functional Specification**

### **Features**

- Spotify login authorization
- Properly queries Spotify API for required information (cover photo, username, playlist song names, etc.)
- Formats a PDF file in a way that can be folded into an aesthetically pleasing handout
- Allow for users to print their handout or email a copy to themselves
- \*Possible extra feature: add some way to share on social media

### **Rough Layout Design**

![alt_text](final-project-design-layour.jpg)

### **Scope of the project**

- Limitations include
  - Create graphics from within the code may be very difficult
  - Spotify authorization issues that may arise
- Assumptions include
  - Spotify will allow users to login in with their accounts
  - Formating graphics and positioning them on a PDF is feasible within the languages being used

## **Brief Timeline**

- Week 1:
  - Write code to query Spotify API for required data (including proper authorization)
  - Error handling for improper queries
  - Create basic Flask server to handle requests from front end
- Week 2:
  - Write code that formats the printout and renders it within the app (this will be very time consuming)
    - Includes rendering cover art, artists and song names, and QR code
  - Create basic screens for the app
- Week 3:
  - Create routing/passing of data between screens
  - Allow vertical flipping of printout so user can see it from multiple angles
  - Add direct printing and email sharing capabilities to the app
- Week 4:
  - Finish all UI components
  - Final touches and bug fixes

## **Rubrics**

All requirements are also in the grading spreadsheets folder linked here: [https://drive.google.com/drive/folders/1JbausO4S1FaXNpDv_7Y0gaGoh6pOSiBL?usp=sharing](https://drive.google.com/drive/folders/1JbausO4S1FaXNpDv_7Y0gaGoh6pOSiBL?usp=sharing)

**Week 1**

<table>
  <tr>
   <td><strong>Category </strong>
   </td>
   <td><strong>Total Score Allocated</strong>
   </td>
   <td><strong>Detailed Rubrics</strong>
   </td>
  </tr>
  <tr>
   <td>Functional
   </td>
   <td>15
   </td>
   <td>
<ul>

<li>4 points: Code successfully connects to Spotify API with authorization 
<ul>
 
<li>2 points: Code connects to API but with improper permissions
 
<li>0 points: No API connection
</li> 
</ul>

<li>4 points: Code successfully retrieves both album and playlist data  
<ul>
 
<li>2 points: Code receives playlist or album data, but not both
 
<li>0 points: No data retrieved from API
</li> 
</ul>

<li>4 points: Code successfully parses retrieved song data into artist name and song name 
<ul>
 
<li>Code partially parses retrieved data, but not in a way that’s usable
 
<li>0 points: Code does not parse retrieved API data
</li> 
</ul>

<li>3 points: Code successfully handles all improper query requests 
<ul>
 
<li>2 points: Code handles some improper requests, but not others
 
<li>0 points: Code cannot handle any improper requests
</li> 
</ul>
</li> 
</ul>
   </td>
  </tr>
  <tr>
   <td>Testing
   </td>
   <td>10
   </td>
   <td>
<ul>

<li>At least 15 unit tests (0.75 points per test)
</li>
</ul>
   </td>
  </tr>
</table>

**Week 2**

<table>
  <tr>
   <td><strong>Category </strong>
   </td>
   <td><strong>Total Score Allocated</strong>
   </td>
   <td><strong>Detailed Rubrics</strong>
   </td>
  </tr>
  <tr>
   <td>Functional
   </td>
   <td>15
   </td>
   <td>
<ul>

<li>4 points: Artist and song names are rendered on the printout properly (15 songs maximum) 
<ul>
 
<li>3 points: “And more!” is not printed at the bottom when a playlist or album has more than 15 songs
 
<li>2 points: artists and song names are rendered on the printout, but not formatted nicely
 
<li>1 point: the wrong amount of artists and song names is rendered (or names bleed off the page)
 
<li>0 points: Artists and song names not rendered on the page at all
</li> 
</ul>

<li>4 points: Cover art and QR code are rendered properly on the printout 
<ul>
 
<li>3 points: QR code rendered on the printout, but not formatted nicely
 
<li>2 points: QR code created but not rendered on screen
 
<li>0 points: no QR code created at all
</li> 
</ul>

<li>3 points: Cut lines and fold lines are rendered properly on the printout 
<ul>
 
<li>2 points: Cut and fold lines are rendered on the printout, but not lined up properly
 
<li>0 points: No cut or fold lines rendered on the page
</li> 
</ul>

<li>4 points: Printout is rendered properly on basic React Native UI screen 
<ul>
 
<li>2 points: printout rendered on screen but not centered
 
<li>0 points: printout not rendered on React Native UI screen
</li> 
</ul>
</li> 
</ul>
   </td>
  </tr>
  <tr>
   <td>Testing
   </td>
   <td>10
   </td>
   <td>
<ul>

<li>At least 10 unit tests (0.5 points each)

<li>At least 5 snapshot tests (1 point each)
</li>
</ul>
   </td>
  </tr>
</table>

**Week 3**

<table>
  <tr>
   <td><strong>Category </strong>
   </td>
   <td><strong>Total Score Allocated</strong>
   </td>
   <td><strong>Detailed Rubrics</strong>
   </td>
  </tr>
  <tr>
   <td>Functional
   </td>
   <td>15
   </td>
   <td>
<ul>

<li>4 points: Create basic UI screens for all pages of the app 
<ul>
 
<li>3 points: 2 out of 3 screens created
 
<li>2 points: 1 out of 3 screens created
 
<li>0 points: no screens reacted 
</li> 
</ul>

<li>4 points: Printout and required data is routed between screens properly 
<ul>
 
<li>2 points: some data missing when routing between screens
 
<li>0 points: no data passed between screens
</li> 
</ul>

<li>3 points: Vertical flipping of printout view implemented 
<ul>
 
<li>0 points: vertical flip not implemented
</li> 
</ul>

<li>4 points: Email and printing functionality of printout implemented 
<ul>
 
<li>3 points: just printing implemented
 
<li>2 points: just sharing via email implemented
 
<li>0 points: neither printing nor email sharing implemented
</li> 
</ul>
</li> 
</ul>
   </td>
  </tr>
  <tr>
   <td>Testing
   </td>
   <td>10
   </td>
   <td>
<ul>

<li>At least 10 unit tests (0.5 points each)

<li>At least 5 snapshot tests (1 point each)
</li>
</ul>
   </td>
  </tr>
</table>

**Week 4**

<table>
  <tr>
   <td><strong>Category </strong>
   </td>
   <td><strong>Total Score Allocated</strong>
   </td>
   <td><strong>Detailed Rubrics</strong>
   </td>
  </tr>
  <tr>
   <td>Functional
   </td>
   <td>15
   </td>
   <td>
<ul>

<li>4 points: Create welcome screen UI 
<ul>
 
<li>2 points: incomplete UI
 
<li>0 points: no UI attempted
</li> 
</ul>

<li>4 points: Create printout viewing screen UI 
<ul>
 
<li>2 points: incomplete UI
 
<li>0 points: no UI attempted
</li> 
</ul>

<li>4 points: Create sharing screen UI 
<ul>
 
<li>2 points: incomplete UI
 
<li>0 points: no UI attempted
</li> 
</ul>

<li>3 points: Implement multi-share button on Share Screen
<ul>
 
<li>2 points: multi-share button attempted but doesn't work
 
<li>0 points: no multi-share button implemented
</li> 
</ul>
</li> 
</ul>
   </td>
  </tr>
  <tr>
   <td>Testing
   </td>
   <td>10
   </td>
   <td>
<ul>

<li>Manual Test Plan (10 pts)
</li>
</ul>
   </td>
  </tr>
</table>
