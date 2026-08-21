# Project: Training Board

## About me
- 2nd-year CS student with a full-time job alongside studies; Saturdays are the
  busiest and most stressful workday.
- Trains an upper/lower split 3x a week and runs at least one 5km a week —
  currently 35 minutes, wants 25–30 without wrecking myself.
- Run data lives in Strava, but Strava presents it as a social feed, not a
  trend I can read progress off. Lifting data lives in a Discord bot I wrote,
  which is a nuisance because it only runs while my laptop is on and I don't
  want to pay for a server.
- Kendo club, reading (novels, light novels, manga) as my study break, music on
  almost constantly. I build alone and don't need an audience for any of it.
- Have written real code: a transit project with a friend (bus stop → next 5
  buses) using Redis, caching, rate limiting. But that's recognition, not
  recall — I know the shape of the problem, I look up the syntax. Comfortable
  in a terminal.
- Doing this to test AI-assisted learning and to build something resume-shaped
  for internship applications.
- ~5 hours a week, aiming for about an hour every other day.

## The idea
A personal training dashboard that pulls my runs from Strava automatically and
lets me log lifting sessions by hand, then shows the trends Strava won't — most
importantly whether my 5km pace is actually improving. It replaces the Discord
bot that dies with my laptop by living on the internet instead, openable from
my phone at the gym. Audience of one, no social features.

## MVP
### In
- Log in with Strava once, granting the app read access to my activities
- Pull my runs and store them: date, distance, time, pace
- A list of my runs, most recent first
- A pace-over-time chart for 5km-ish runs
- Log a lifting session by hand: date, exercise, weight, reps
- A list of my lifting sessions
- Deployed and live on the internet, openable from my phone

### Parking lot (v2)
- The contribution-style grid (a visual layer over data the MVP already has)
- Personal records and PR detection
- Editing and deleting past lifting entries
- Volume-per-muscle-group tracking across the upper/lower split
- Filtering runs by distance, weather, route
- Predicted finish times and goal pacing
- Scheduled background sync (MVP syncs on page load instead — simpler, cheaper,
  same result)
- Anything about reading, music, or kendo

## The trunk — core components

### Source control (git + GitHub)
The save-and-undo system professionals use — snapshots of the project so I can
see what changed and go back when something breaks. In from day one, before
there's anything to save, and it's also where an interviewer will look.

### The frontend — the page I look at
What renders in Safari: the run list, the pace chart, the form for entering a
lifting set. Runs on my device, holds no data of its own, asks for everything.

### The backend — my code running on a machine
The part with no visual appearance. Talks to Strava, decides what to store,
answers the frontend's questions. Same idea as my Discord bot, with a face on
it. Most of the learning lives here.

### The database — where things persist
Where runs and lifting sets survive after everything shuts down. Without it,
closing the app means starting over.

### Talking to Strava (the API and the permission flow)
An API is the doorway another company opens so programs can ask their system
for things. Strava's lets me request my activities. The permission flow (OAuth)
is how Strava learns I'm allowed to ask — I approve once on Strava's own page,
my password never touches my app, and access is narrow (read activities only)
and revocable. The most transferable piece in the project.

### How the pieces talk (HTTP requests)
Everything above communicates by sending small messages over the internet: a
request goes out, a response comes back. Frontend → backend. Backend → Strava.
Same mechanism both times.

### Secrets and configuration
Strava keys and the database address — values the code needs that must never be
written into the code or pushed to GitHub. Kept in a file listed in
`.gitignore`, loaded when the app starts.

### Deployment — getting it onto the real internet
Moving the backend and database off my laptop onto a machine that stays awake,
with an address I can open from my phone at the gym. The thing the Discord bot
never had. Free tiers cover an app this small — we verify the actual terms the
week we deploy.

## Mental model to keep
Logging one squat set at the gym touches five of the eight pieces: the browser
on my phone sends it to the backend over an HTTP request, the backend writes it
to the database, and it works away from my laptop only because it's deployed.
Strava isn't involved at all in that path — that's runs only.
