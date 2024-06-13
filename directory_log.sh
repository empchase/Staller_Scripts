# log of commands run

# June 11
# goal: get github to work 

#run from any directory
git config --global user.name "empchase"
git config --global user.email "empchase@berkeley.edu"
git config --global --list
	user.name=empchase
    user.email=empchase@berkeley.edu

cd /global/scratch/users/empchase/Scripts/
git init
	Initialized empty Git repository in /global/scratch/users/empchase/Scripts/.git/

# Created new git repository: Staller_Scripts, initialized with repository

git remote add origin https://github.com/empchase/Staller_Scripts.git
git remote -v
	origin	https://github.com/empchase/Staller_Scripts.git (fetch)
    origin	https://github.com/empchase/Staller_Scripts.git (push)

git push -u origin main
	Gtk-WARNING **: 11:47:29.237: cannot open display: 
    error: unable to read askpass response from '/usr/libexec/openssh/gnome-ssh-askpass'
    Username for 'https://github.com': empchase


	Gtk-WARNING **: 11:47:40.958: cannot open display: 
    error: unable to read askpass response from '/usr/libexec/openssh/gnome-ssh-askpass'
    Password for 'https://empchase@github.com': 
    fatal: Authentication failed for 'https://github.com/empchase/Staller_Scripts.git/'

# June 12
# goal: get github to work. try implementing token for login

# generated token for login 

git push -u origin main
    #input token as password
    error: src refspec main does not match any.
    error: failed to push some refs to 'https://github.com/empchase/Staller_Scripts.git'

#nothing visible on my github
# tried the above again in case I just put my token in wrong or something
# same error thrown

# try another way
git add .
git commit -m "Script Commit 20240612"
     58 files changed, 248594 insertions(+)
    create mode 100644 ciber_experiment/ADscripts/ADreadsmapper.py
    create mode 100644 ciber_experiment/ADscripts/Makefile
    create mode 100644 ciber_experiment/ADscripts/make.sh
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18589709.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592280.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592292.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592294.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592297.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592299.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592311.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/ADreadsmapper_tests/slurm-18592372.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18587522.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589636.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589639.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589663.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589666.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589667.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589668.out
    create mode 100644 ciber_experiment/ADscripts/old_slurm/test_script/slurm-18589672.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18592478.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18593109.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18593114.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18593115.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18593116.out
    create mode 100644 ciber_experiment/ADscripts/slurm-18593119.out
    create mode 100644 ciber_experiment/ADscripts/test_script.py
    create mode 100644 ciber_experiment/RPTRscripts/.ipynb_checkpoints/RPTRstats-checkpoint.ipynb
    create mode 100644 ciber_experiment/RPTRscripts/Makefile
    create mode 100644 ciber_experiment/RPTRscripts/RPTRSTATS.csv
    create mode 100644 ciber_experiment/RPTRscripts/RPTRreadsmapper.py
    create mode 100644 ciber_experiment/RPTRscripts/RPTRstats.ipynb
    create mode 100644 ciber_experiment/RPTRscripts/make.sh
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599187.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599190.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599191.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599193.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599194.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18599648.out
    create mode 100644 ciber_experiment/RPTRscripts/old_slurm/slurm-18600150.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18640724.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18652851.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18652891.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18652952.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18711855.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18712253.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18712257.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18739928.out
    create mode 100644 ciber_experiment/RPTRscripts/slurm-18741899.out
    create mode 100644 gzip/gzip.sh
    create mode 100644 gzip/slurm-15420675.out
    create mode 100755 mapper/step1mapper.py
    create mode 100755 mapper/step1mapper.sh
    create mode 100644 pear/Makefile
    create mode 100644 pear/make.sh
    create mode 100644 pear/pear.sh
    create mode 100644 split/Sfile.sh
    create mode 100644 split/Sfile_EC.sh
    create mode 100644 split/Sfiles.py

git push origin main
    Password for 'https://empchase@github.com': 
    error: src refspec main does not match any. #same error
    error: failed to push some refs to 'https://github.com/empchase/Staller_Scripts.git'

git status
    # On branch master nothing to commit, working directory clean
git add split/Sfiles.py
git status
    # On branch master nothing to commit, working directory clean
git init
    Reinitialized existing Git repository in /global/scratch/users/empchase/Scripts/.git/
git status
    # On branch master nothing to commit, working directory clean
git add split/Sfiles.py
git status
    # On branch master nothing to commit, working directory clean
git log
    commit b18888ee5c8c93dd5eb05e55b5077362bc4b1f10
    Author: empchase <empchase@berkeley.edu>
    Date:   Wed Jun 12 19:19:55 2024 -0700

        Script Commit 20240612


git branch
git push -u origin master
    Counting objects: 67, done.
    Delta compression using up to 20 threads.
    Compressing objects: 100% (64/64), done.
    Writing objects: 100% (67/67), 180.97 KiB | 0 bytes/s, done.
    Total 67 (delta 25), reused 0 (delta 0)
    remote: Resolving deltas: 100% (25/25), done.
    remote: 
    remote: Create a pull request for 'master' on GitHub by visiting:
    remote:      https://github.com/empchase/Staller_Scripts/pull/new/master
    remote: 
    remote: To https://github.com/empchase/Staller_Scripts.git
    * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.

