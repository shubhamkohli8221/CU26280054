# Linux Administration

Linux command-line and administration laboratory exercises for the Master of
Computer Applications programme.

## Requirements

- A Linux installation, virtual machine, or container with Bash.
- `sudo` access for exercises that create users, groups, packages, mounts, or
  filesystems.
- An Ubuntu/Debian environment for `apt` exercises.
- A Fedora/RHEL-based environment for `rpm` and `dnf` exercises.
- `vim` for Lab Sheet 5 and `setfacl`/`getfacl` for Lab Sheet 6.
- `tar`, `gzip`, `zip`, and `unzip` for Lab Sheet 9.

Commands that change system state should be run only in a disposable lab
environment. Read each command before running it, especially commands using
`sudo`, `rm -rf`, `mkfs`, `mount`, `userdel`, or `dnf remove`.

## Lab Sheets

| Lab sheet | Topics | Exercises |
| --- | --- | ---: |
| [Lab Sheet 1](lab_sheet_01.txt) | Files, permissions, users, processes, jobs, packages, services, ownership, `nice`, and basic shell commands | 50 |
| [Lab Sheet 2](lab_sheet_02.txt) | Bash variables, input, arithmetic, conditions, loops, arguments, redirection, pipelines, logging, and error handling | 20 |
| [Lab Sheet 3](lab_sheet_03.txt) | User and group identification, account creation, passwords, shells, home directories, locking, expiry, and cleanup | 20 |
| [Lab Sheet 4](lab_sheet_04.txt) | Navigation, file and directory operations, searching, text processing, permissions, disk usage, and command help | 50 |
| [Lab Sheet 5](lab_sheet_05.txt) | `vim` editing, movement, insertion, search, substitution, copying, undo/redo, and saving | 20 |
| [Lab Sheet 6](lab_sheet_06.txt) | Permission modes, `umask`, access control lists, default ACLs, and permission testing | 20 |
| [Lab Sheet 7](lab_sheet_07.txt) | Disk usage, block devices, filesystems, loopback devices, partitioning, mounting, and unmounting | 20 |
| [Lab Sheet 8](lab_sheet_08.txt) | Process inspection, `top`/`htop`, background jobs, signals, stopping/continuing processes, and cleanup | 20 |
| [Lab Sheet 9](lab_sheet_09.txt) | `tar`, gzip, ZIP archives, extraction, verification, and backup workflows | 20 |
| [Lab Sheet 10](lab_sheet_10.txt) | RPM queries, DNF repositories, searching, installation, updates, removal, verification, and history | 20 |
| [Lab Sheet 11](lab_sheet_11.txt) | ext4 filesystems, UUIDs, `/etc/fstab`, persistent mounts, filesystem checks, and loopback cleanup | 20 |

## How to use the sheets

1. Open the relevant text file.
2. Run each question's commands from a suitable working directory.
3. Replace placeholders such as `<PID>`, `<package>`, and usernames with
   values from your environment.
4. Verify the output after each command instead of running the entire sheet
   as one script.
5. Complete the cleanup commands at the end of workflows so test users,
   groups, loop devices, mounts, and temporary files are removed.

The commands are intentionally presented as practice prompts rather than
ready-to-run scripts. Some examples assume files or directories created by
earlier questions in the same lab sheet.
