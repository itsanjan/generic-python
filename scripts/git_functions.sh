# https://coderwall.com/p/9idt5g/keep-your-feature-branch-up-to-date
# Add this to bashrc to hyper-automate
# https://hackernoon.com/git-merge-vs-rebase-whats-the-diff-76413c117333
function update(){
  git checkout master && git pull && git checkout - && git rebase master
}
