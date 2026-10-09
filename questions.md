# HackCyros 4.0 — MULTIVERSE COLLAPSED
### CTF Challenge Design Document · Theme: Avengers: Doomsday

> Format: Jeopardy-style · 28 challenges · 8 categories · 3 waves
> Flag format: `HC4{<Leet_Phrase>_<12-hex-salt>}` (mixed case + leetspeak + random salt, no spaces; see §9)

---

## 1. Master Story

**Premise:** Doctor Doom's final move has fractured the multiverse. The Avengers' central archive, **the Sanctum Mainframe**, is leaking across realities, and the only people who can patch it are *you*: the freshly recruited **"Variant Hackers"** from Universe-CUJ.

**Overarching mystery:** Someone planted a backdoor, the **"Variant Zero"**, that triggered the collapse. Nobody knows who they are, why they did it, or whether they meant to. Each wave drops more clues about them.

**Hidden twist (reveal only after Wave 3):** Variant Zero is a clumsy intern from Universe-616-B who ran `rm -rf /multiverse` while "just cleaning up temp files". Doom did not break the multiverse; Doom *exploited* it. The twist is funny and tragic at the same time.

### Tone ladder (the core design rule)

| Wave | Difficulty | Name | Funny | Mystery | Feel |
|---|---|---|---|---|---|
| 1 | Easy | **The Cracks Appear** | ███████ high | ██ low | Slapstick, memes, "oops" energy. Clues are almost given away. |
| 2 | Medium | **Incursions** | ████ medium | ████ medium | Banter plus real suspects. Stories link to each other. |
| 3 | Difficult | **Doomsday** | ██ dark humor | ███████ high | Tense. Humor appears only as gallows jokes. Answers feed the final reveal. |

**Rule for authors:** every challenge needs (a) a 3-5 sentence story, (b) one joke or absurd detail, (c) one mystery thread that points to Variant Zero or the next challenge.

---

## 2. Distribution

| Category | Easy | Medium | Difficult | Total |
|---|:-:|:-:|:-:|:-:|
| Web | 2 | 2 | 1 | 5 |
| OSINT | 2 | 2 | 1 | 5 |
| Crypto | 1 | 2 | 1 | 4 |
| Forensics | 1 | 2 | 1 | 4 |
| Reverse | 1 | 1 | 1 | 3 |
| Steganography | 1 | 1 | 1 | 3 |
| Misc | 1 | 1 | 0 | 2 |
| Binary/Pwn | 0 | 1 | 1 | 2 |
| **Total** | **9** | **12** | **7** | **28** |

**Points:** Easy 100–200 · Medium 250–400 · Difficult 450–600
**Wave unlock (CTFd):** Wave 2 opens at 20 min or after any 15 total solves; Wave 3 opens at 70 min or after any 30 total solves. Adjust to your event length.

---

## 3. Wave 1 — EASY: *The Cracks Appear* (9 challenges)

**Wave story:** Reality starts glitching. Nobody is panicking yet, and most problems are caused by the Avengers' own sloppy IT.

---

### E01 · Fury's Eyes Only — **Web** · 100 pts
- **Story:** Nick Fury put his secret files on a website and wrote "DO NOT LOOK" in the robots file. Pure genius.
- **Concept:** `robots.txt` → hidden path → flag in HTML comment.
- **Solve path:** `/robots.txt` → `/fury-eyes-only` → view-source.
- **Joke:** Page title says "404: Eye Not Found" even though it is a 200.
- **Mystery thread:** Page footer lists the last editor: `variant_0`.
- **Flag:** `HC4{Fury_F0rg0t_Th3_Ey3_P4tch_0n_R0b0ts_44abc7813935}`

### E02 · Stark Intern Login — **Web** · 150 pts
- **Story:** Happy Hogan left Tony's intern portal unguarded. The intern's password is "whatever Pepper said."
- **Concept:** Basic SQL injection login bypass.
- **Solve path:** `' OR 1=1 --` on the login form → dashboard shows the flag.
- **Joke:** The error message says "Pepper would not approve of this query."
- **Mystery thread:** The dashboard shows a deleted user "Variant Zero, last login: Universe-616-B".
- **Flag:** `HC4{P3pp3r_W0uld_N0t_Appr0v3_Th1s_Qu3ry_59514e669f03}`

### E03 · Where's Thor? — **OSINT** · 150 pts
- **Story:** Thor posted a "chill day" photo and vanished. Find the exact café he was seen at.
- **Concept:** Image reverse search plus landmark geolocation. Build a fake profile with a photo taken near a real recognizable landmark.
- **Solve path:** Reverse image search → cafe name → flag is `HC4{<cafe_name_snake_case>}`.
- **Joke:** Caption: "Mjolnir is on charging, back in 5."
- **Mystery thread:** Reflection in the cafe window shows a figure with a hoodie and the text `616-B`.
- **Flag:** `HC4{Th0r_Sipp3d_4t_<Cafe_Name>_1f52fa70c01c}` (fill after photo is chosen)

### E04 · Wakanda DNS Records — **OSINT** · 200 pts
- **Story:** Shuri says Wakanda's secret site is not hidden, just "misconfigured." Find what she forgot.
- **Concept:** DNS TXT record on a domain you own.
- **Solve path:** `dig TXT` or an online DNS tool → flag in the TXT record.
- **Joke:** TXT says "Shuri: do not tell T'Challa I forgot to remove this."
- **Mystery thread:** A second subdomain `variant0.<domain>` exists, left for Wave 2 (E-M03).
- **Flag:** `HC4{Shur1_S4ys_DNS_1s_N0t_V1br4n1um_f1282975fd80}`

### E05 · Groot Speaks — **Crypto** · 100 pts
- **Story:** Groot sent an urgent message. The Avengers' translator is broken. Decode it before Rocket eats the printout.
- **Concept:** Substitution encoding: "I am Groot" variants map to binary → ASCII.
- **Solve path:** Count "I"/"i" casing as bits → decode.
- **Joke:** The final decoded message includes "I am Groot" as the last word.
- **Mystery thread:** The message begins with "Variant seen near the Mind Stone..."
- **Flag:** `HC4{I_4m_Gr00t_4nd_1_4m_B4s3_Tw0_7adb9d5e4089}`

### E06 · Black Box Dropbox — **Forensics** · 150 pts
- **Story:** S.H.I.E.L.D. recovered a file called `evidence.jpg`. It will not open. Hawkeye says "it looks like a very sad JPG."
- **Concept:** Wrong extension / file signature check, `file`, `strings`, EXIF.
- **Solve path:** `file evidence.jpg` → actually a ZIP → inside a text file with the flag; EXIF comment holds the ZIP password hint.
- **Joke:** EXIF camera model: "Hawkeye's Disposable Camera."
- **Mystery thread:** Timestamp matches the moment the multiverse first glitched.
- **Flag:** `HC4{H4wk3y3_N3v3r_M1ss3s_4_F1l3_S1gn4tur3_1e2e3c9dc0d9}`

### E07 · Ant-Man's Tiny Crackme — **Reverse** · 150 pts
- **Story:** Scott Lang wrote a license-checker so tiny that it fits in 1 KB. It only accepts the "quantum password."
- **Concept:** `strings`, `ltrace`, or a simple disassembly check.
- **Solve path:** Password is stored in plain form or a one-step XOR.
- **Joke:** Failure message: "Wrong. Hope Pym is disappointed."
- **Mystery thread:** The binary contains a compile path `/home/variant0/`.
- **Flag:** `HC4{Sm4ll_B1n4ry_B1g_R3gr3t_b3af9d9941f0}`

### E08 · Hulk Smash Pic — **Steganography** · 150 pts
- **Story:** Banner left a picture of Hulk "looking calm" before he got angry. The picture is calm, too calm.
- **Concept:** Data appended after the image end marker, or a basic LSB with `zsteg`.
- **Solve path:** `binwalk` / `strings` / `zsteg` → hidden message.
- **Joke:** Hidden text: "HULK HIDE MESSAGE. HULK NOT GOOD AT HIDING."
- **Mystery thread:** Extra line: "Seen at Sanctum, 3 AM."
- **Flag:** `HC4{HULK_H1d3_M3ss4g3_Hulk_N0t_G00d_97bc7b385d30}`

### E09 · Sanity Check at the Sanctum — **Misc** · 100 pts
- **Story:** Doctor Strange agrees to give you a free flag if you prove you can read the rules and answer one riddle through a time loop.
- **Concept:** Rules-page flag plus a short chain decoding (Base64 → Hex → ROT13).
- **Solve path:** Decode the nested string in the rules text.
- **Joke:** Strange: "I have looped this conversation 14,000,605 times. Just decode it."
- **Mystery thread:** One of the loop counts differs from the rest, which hints someone else is in the loop.
- **Flag:** `HC4{Str4ng3_L00p_S4n1ty_Ch3ck_P4ss3d_d9302d4a80e8}`

---

## 4. Wave 2 — MEDIUM: *Incursions* (12 challenges)

**Wave story:** Universes begin colliding. The jokes get sharper and the suspects multiply: the Illuminati, a rogue Wanda, and a Thunderbolts defector. All evidence points toward an inside job.

---

### M01 · Multiverse Cookie Jar — **Web** · 300 pts
- **Story:** The Multiverse Passport Office issues cookies as visas. Yours says "Tourist." The flag says "Sorcerer Supreme."
- **Concept:** JWT with weak secret or `alg: none`.
- **Solve path:** Decode token → forge `role: sorcerer_supreme` → access `/vault`.
- **Joke:** Every wrong attempt returns a different universe's error: "404 in Universe-199999."
- **Mystery thread:** Token issuer field: `variant_zero@616-B`.
- **Flag:** `HC4{JWT_V1s4_St4mp3d_By_Wr0ng_Str4ng3_34308f2df9da}`

### M02 · Variant Verification Portal — **Web** · 350 pts
- **Story:** Each Variant has a profile ID. Fury wants the profile of Variant Zero, but the portal only shows yours.
- **Concept:** IDOR with predictable/hashed IDs (e.g. `md5(n)`).
- **Solve path:** Notice ID pattern → enumerate → find the profile whose bio mentions the flag.
- **Joke:** Bio field: "Occupation: Professional Mistake-Maker."
- **Mystery thread:** Bio mentions a pager number reused in M03 and M11.
- **Flag:** `HC4{1D0R_Th3_1nt3rn_D1d_1t_4g41n_58cddae0c409}`

### M03 · The Variant Who Fled — **OSINT** · 300 pts
- **Story:** Variant Zero ran. A scrubbed GitHub repo, an old commit and a forgotten email are all that remain.
- **Concept:** Git history leaks, Wayback Machine, username pivoting.
- **Solve path:** Repo commit email → username → archived blog post → flag in the post.
- **Joke:** Commit message: "fixed it (it was not fixed)."
- **Mystery thread:** Blog says: "I only wanted to clean up the temp folder."
- **Flag:** `HC4{G1t_Bl4m3_P01nts_T0_Th3_1nt3rn_0a6e78f6a67c}`

### M04 · Sokovia Paper Trail — **OSINT** · 350 pts
- **Story:** A leaked Accords draft has hidden metadata. Who wrote it, and where did they print it?
- **Concept:** PDF metadata, revision history, photo geolocation of a scanned page.
- **Solve path:** Author/producer → location of the printer from EXIF in an embedded image.
- **Joke:** Author field: "Definitely not Tony Stark."
- **Mystery thread:** Edit timestamps show someone from another timezone edited it.
- **Flag:** `HC4{4cc0rds_S1gn3d_By_Wr0ng_Auth0r_66205c35cda0}`

### M05 · Vision's Mind Stone RSA — **Crypto** · 350 pts
- **Story:** The Mind Stone's encryption was set up by someone who "skimmed the RSA chapter."
- **Concept:** RSA with small `e` and no padding, or two primes close together (Fermat).
- **Solve path:** Recover `n` factorization → decrypt.
- **Joke:** Public key comment: "p and q chosen at random (they are neighbours)."
- **Mystery thread:** Plaintext includes "Mind Stone cracked from inside."
- **Flag:** `HC4{V1s10n_S4ys_Ch00s3_Pr1m3s_F4r_4p4rt_a41e0463ca50}`

### M06 · Loki's Lies — **Crypto** · 300 pts
- **Story:** Loki "encrypted" his confession with a very short key, then lied about it being long.
- **Concept:** Repeating-key XOR with known plaintext prefix `HC4{`.
- **Solve path:** Crib-drag with `HC4{` → get the key → decrypt.
- **Joke:** Key: `TRUSTME`.
- **Mystery thread:** Decrypted text names two possible traitors, a misdirection.
- **Flag:** `HC4{Gl0r10us_Purp0s3_Sh0rt_X0R_K3y_a86ee8b7509b}`

### M07 · Quantum Realm Pcap — **Forensics** · 350 pts
- **Story:** Someone exfiltrated files from the Quantum Realm over the network. All you have is a capture.
- **Concept:** Wireshark, follow streams, export HTTP objects, reassemble.
- **Solve path:** Find HTTP POST with a base64 chunked file → reassemble.
- **Joke:** User-Agent: `AntMan/0.0.1-tiny`.
- **Mystery thread:** Destination IP resolves to the same domain as in E04.
- **Flag:** `HC4{P4ck3ts_Shr1nk_But_H34d3rs_D0nt_L13_f5550af1e73b}`

### M08 · Deleted Scenes — **Forensics** · 400 pts
- **Story:** The Avengers' archive shows a deleted scene from the first Incursion. Recover it.
- **Concept:** Disk image analysis and file carving (Autopsy / `photorec`).
- **Solve path:** Mount image → find deleted entry → recover → read flag.
- **Joke:** Folder name: "Definitely Not Evidence."
- **Mystery thread:** A recovered note lists a meeting with "D.D." (Doctor Doom).
- **Flag:** `HC4{D3l3t3d_But_N0t_R34lly_G0n3_539b96c6554c}`

### M09 · Strange's Time Loop — **Reverse** · 400 pts
- **Story:** Strange's spell is a function that loops until the key is right. Nobody has escaped the loop.
- **Concept:** Obfuscated loop with arithmetic transformations; static analysis plus patching or scripting.
- **Solve path:** Reverse the transform in Python → derive the input.
- **Joke:** Output on a wrong key: "Dormammu, I've come to bargain... again."
- **Mystery thread:** Loop counter constant `616` equals the universe label.
- **Flag:** `HC4{1_H4v3_C0m3_T0_B4rg41n_W1th_R3v3rs1ng_d460a495c4db}`

### M10 · Shuri's Spectrogram — **Steganography** · 300 pts
- **Story:** Shuri sends an audio note called "totally normal music." It sounds like a dial-up modem in a thunderstorm.
- **Concept:** Hidden text in an audio spectrogram, plus a Morse segment.
- **Solve path:** Audacity/Sonic Visualiser → spectrogram → text; Morse as a second layer.
- **Joke:** Spectrogram shows a tiny panther, then the flag.
- **Mystery thread:** Morse says: "Someone has Wanda's cooperation."
- **Flag:** `HC4{Shur1_H1d3s_Fl4gs_1n_Fr3qu3ncy_de05b9395000}`

### M11 · JARVIS Jail — **Misc** · 350 pts
- **Story:** JARVIS is locked in a restricted Python sandbox. It must retrieve the flag, but half of its builtins were "removed for safety."
- **Concept:** Python jail escape with restricted builtins (e.g. via `__class__`/`__subclasses__` chains).
- **Solve path:** Escape via object introspection → read `flag.txt`.
- **Joke:** Blocked-word message: "Sir, that is not a very Stark thing to import."
- **Mystery thread:** A hidden log entry shows the pager number from M02.
- **Flag:** `HC4{S1r_1_H4v3_3sc4p3d_Th3_S4ndb0x_8a23ccb4f757}`

### M12 · Stack of Shields — **Binary/Pwn** · 400 pts
- **Story:** Cap's shield stack has a classic flaw: too many shields, too little memory.
- **Concept:** Stack buffer overflow to a `win()` function (no PIE, no canary).
- **Solve path:** Find offset → overwrite return → call `win`.
- **Joke:** Prompt: "Enter shield count (Cap can lift up to 64):"
- **Mystery thread:** Win function name: `avengers_assemble_variant0`.
- **Flag:** `HC4{1_C4n_D0_Th1s_4ll_D4y_R3t2W1n_c2cb36812877}`

---

## 5. Wave 3 — DIFFICULT: *Doomsday* (7 challenges)

**Wave story:** Doom is at the gates. The infrastructure is on fire, the clues converge, and every challenge reveals a piece of the final truth. The humor turns black; the mystery turns urgent.

---

### D01 · Doom's Gate — **Web** · 550 pts
- **Story:** Doom's Latverian portal guards the Multiverse Core behind three doors: a public form, an internal service, and a final bureaucrat.
- **Concept:** Multi-step chain: SSRF → internal-only admin panel → template injection (SSTI) for RCE.
- **Solve path:** URL fetch feature → SSRF bypass → internal panel → SSTI → read flag.
- **Joke:** Each door has a "Doom is not responsible for your emotional damage" notice.
- **Mystery thread:** Internal panel shows a log: "Variant Zero opened door 1 by accident."
- **Flag:** `HC4{D00m_D03s_N0t_D0_1nput_V4l1d4t10n_7d00e4eef97f}`

### D02 · Find Variant Zero — **OSINT** · 500 pts
- **Story:** The last stand. Every clue from earlier waves points to a person. Combine them and find where Variant Zero is hiding.
- **Concept:** Multi-source OSINT with custom-built personas (Python-generated profiles, archived pages, geolocation).
- **Solve path:** Pager number + username + timezone + archived page → locate the hiding place.
- **Joke:** Their last post: "Did anyone else's multiverse just… stop?"
- **Mystery thread:** This one hands the player the first full piece of the twist.
- **Flag:** `HC4{V4r14nt_Z3r0_W4s_Just_4n_1nt3rn_f499a3da1072}`

### D03 · Doom's Padding — **Crypto** · 550 pts
- **Story:** Doom's messages are AES-CBC protected. The server helpfully tells you if the padding is wrong. Thank you, Doom.
- **Concept:** CBC padding oracle attack.
- **Solve path:** Script the oracle byte-by-byte → recover plaintext.
- **Joke:** Server error: "Invalid padding. Doom is disappointed in your form."
- **Mystery thread:** Plaintext is Doom's memo: "Intern's mistake has saved me years of work."
- **Flag:** `HC4{D00m_L34ks_1nf0_W1th_P4dd1ng_3rr0rs_5ef66b867947}`

### D04 · Memory of the Multiverse — **Forensics** · 550 pts
- **Story:** A memory dump from the Sanctum Mainframe, taken seconds before collapse. Something unusual was running.
- **Concept:** Volatility: process list, injected code / hidden process, key extraction, decrypt a file.
- **Solve path:** Find suspicious process → dump memory → extract key → decrypt provided artifact.
- **Joke:** A process named `definitely_not_malware.exe`.
- **Mystery thread:** The command line shows the exact `rm -rf` that started it.
- **Flag:** `HC4{rm_rf_Sl4sh_Mult1v3rs3_48a926bb6b2b}`

### D05 · Time Stone VM — **Reverse** · 600 pts
- **Story:** The Time Stone runs on a tiny virtual machine. Nobody has the spec. Make one up from the bytecode.
- **Concept:** Custom VM reversing: opcodes → disassembler → solve the constraint.
- **Solve path:** Write a disassembler → emulate → recover the input via Z3 or manual inversion.
- **Joke:** Opcode names: `REWIND`, `UNDO`, `OOPS`.
- **Mystery thread:** The last instruction block is labeled `variant0_final_commit`.
- **Flag:** `HC4{T1m3_1s_Just_4_R3g1st3r_a53be4c9c402}`

### D06 · Scarlet Witch's Reality Layers — **Steganography** · 500 pts
- **Story:** Wanda rewrote reality three times. Each rewrite hides another layer. Peel them in the right order.
- **Concept:** Multi-layer chain: PNG LSB (with a key) → audio file → password-protected ZIP.
- **Solve path:** Layer 1 key from earlier challenges (M10 Morse) → layer 2 → layer 3 → flag.
- **Joke:** Layer names: "Reality 1, Reality 2, No More Mutants."
- **Mystery thread:** Final layer shows Wanda's note: "I only fixed what the intern broke."
- **Flag:** `HC4{N0_M0r3_L4y3rs_W4nd4_1s_D0n3_5a2f55145a0a}`

### D07 · Doomsday Heap — **Binary/Pwn** · 600 pts
- **Story:** The Doomsday device runs on a custom allocator. Every allocation is a regret.
- **Concept:** Format string leak (PIE/ASLR defeat) → ROP or heap manipulation for shell.
- **Solve path:** Leak libc → compute base → build chain → shell → `cat flag.txt`.
- **Joke:** Banner: "DOOM ALLOCATOR v0.1: no free, only regret."
- **Mystery thread:** Final comment in the source: `// TODO: intern, please never touch this`.
- **Flag:** `HC4{D00m_M4ll0c_1s_St1ll_Just_M4ll0c_f48bd875c389}`

---

## 6. Lore Reveal (post-Wave 3)

Give each team a **Lore Fragment** per wave, shown after they solve **any 5 / 8 / 4** challenges from Waves 1 / 2 / 3 respectively. Collecting all three shows the final screen:

1. **Fragment I (Wave 1):** "The glitches began at 3 AM in Universe-616-B."
2. **Fragment II (Wave 2):** "Doom's allies thought Variant Zero was a traitor. They were wrong."
3. **Fragment III (Wave 3):** "One intern. One command. One terrible Tuesday."

Final screen: **"The multiverse was not destroyed by a villain. It was destroyed by a Tuesday."**

---

## 7. Authoring Checklist

- [ ] Every challenge has a story, a joke, and a mystery thread.
- [ ] Easy challenges solvable by a first-year with Google in ≤ 15 minutes.
- [ ] Medium needs at least one tool or script; ≤ 40 minutes for a decent team.
- [ ] Difficult has a unique first-solve path; no unintended shortcuts.
- [ ] No challenge requires brute-forcing the platform or other infrastructure.
- [ ] Each challenge tested on a clean machine by someone who did NOT write it.
- [ ] Flags are unique per challenge, no reuse, no leaks in file names or metadata.
- [ ] Every flag follows the Flag Policy (§9) and is embedded exactly as listed.
- [ ] 2 hints per challenge (cost: 10% / 25% of points).
- [ ] Docker/service challenges (Web, Pwn) have resource limits and auto-restart.
- [ ] Writeups prepared before the event, with author contact for disputes.

## 8. Cross-Challenge Clue Map

| Clue | Planted in | Used in |
|---|---|---|
| `variant0.<domain>` subdomain | E04 | M03 |
| Pager number | M02 | M11, D02 |
| `616-B` universe tag | E03, E07, M01 | D02 |
| Morse note (stego key) | M10 | D06 |
| Doom memo | M08 | D03 |
| `rm -rf` command | D04 | Lore reveal |

## 9. Flag Policy

- **Format:** `HC4{<Leet_Phrase>_<12-hex-salt>}`, e.g. `HC4{Fury_F0rg0t_..._a3f91c07bd42}`.
- **Phrase:** mixed case + leetspeak + underscores, tied to the challenge story (helps writeups, but the salt blocks guessing).
- **Salt:** 12 random hex chars generated with `secrets.token_hex(6)`, so a team cannot guess a flag from the story or from another team's partial leak.
- **Per-team flags (optional, strongly recommended for Web/Pwn):** CTFd dynamic flags or a per-team salt to detect flag sharing.
- **Case-sensitive:** set all flags case-sensitive in CTFd.
- **Length:** 40-70 characters. Longer than that causes copy/paste errors at the venue.
- **Placeholder:** E03's `<Cafe_Name>` must be replaced with the real café name (snake_case, leetspeak optional) once the photo is final. Keep the salt.
- **Re-roll rule:** if any flag appears in a screenshot, repo or chat before the event, regenerate its salt.