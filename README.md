# Evergreen Atoms

Small programs and scripts made to support Evergreen contributions.

## Fix Double Announcement of Icon Labels

Path: `src/fix_double_announcement.py`

This script processes HTML files to resolve accessibility issues where screen readers announce icon button and link labels twice. The problem arises due to the presence of both aria-label and title attributes on tags that contain Material icons. The script moves the title attribute to the inner span with the material-icons class, preventing double announcements while preserving tooltips.

### Bug Reference

This script addresses the issue described in [Launchpad Bug 2075362](https://bugs.launchpad.net/evergreen/+bug/2075362). The bug causes screen readers to announce icon button and link labels twice due to the simultaneous presence of aria-label and title attributes.