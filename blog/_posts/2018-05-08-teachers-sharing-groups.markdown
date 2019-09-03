---
title: Teachers Sharing Groups
description: Allowing multiple teachers to share a group.
author: James Sharkey
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James is a physicist turned computer scientist, working both on physics and computing for Isaac
author_site: https://isaacphysics.org/about
---
One question we get asked fairly frequently by teachers is about sharing an Isaac group with their colleagues; until now, we've had to answer that it's not possible and offer some clunky workarounds. We're now internally testing the ability to add other teachers as additional managers for groups!

This would allow those managers to see student progress on all assignments set to the group, set new assignments to the group themselves and invite additional students to the group just as group owners can. We'll hopefully launch it as an opt-in beta feature next month, and have it ready for all teachers in time for the next academic year!
<br>[<b>Update August 2019:</b> This is now available to all teachers.]

Why has this been so tricky to implement? Our data sharing model puts students in control of their data; they have to opt-in to sharing data with teachers explicitly, and can revoke this access at any time. It's this one-to-one student to teacher link, but many-to-one teacher to group link, that has made things complicated; but we think we've now got a system that works.

<figure style="text-align:center;margin:15px auto 25px auto;width:90%;">
    <img src="/images/sharing-groups/auth-dialogue-box.png" alt="The new sharing confirmation dialogue box, listing the names and emails of all teachers who manage the group.">
    <figcaption>We've updated the confirmation dialogue when you use a group code to list all teachers who can access that group's data. Teachers you already share some data with are shown in green.</figcaption>
</figure>

When students use a group code, they'll now see a more detailed dialogue like the one above, showing all the teachers they will be granting access to. It also highlights those they are already sharing some data with: to show that they have trusted that user before, or to help see which additional managers have been added since they last used the group code.

How do you use this new feature? Teachers will eventually be given a new option alongside the "Invite Users" option for groups they have created: "Edit Group Managers":
<figure style="text-align:center;margin:15px auto 25px auto;width:90%;">
    <img src="/images/sharing-groups/add-managers-dialogue-box.png" alt="The new edit group manager interface, listing the names and emails of all teachers who manage the group.">
    <figcaption>Group owners will be able to add colleagues with teacher accounts to their groups.</figcaption>
</figure>

The additional managers may be colleagues who teach the same class, heads of department or even headteachers; the only conditions are that they have a teacher account on Isaac and the students approve access to them. Students must approve access to _all_ of the additional managers and the owner of a group in order to join that group; only teachers that students could reasonably expect to have access to their data should be added.

One issue we expect to see when adding group managers _after_ some students have joined the group is that these group managers will not be able to see some student progress.
<figure style="text-align:center;margin:15px auto 25px auto;width:90%;">
    <img src="/images/sharing-groups/group-student-list.png" alt="A list of students ion the group; only one of them has approved access to this additional manager.">
    <figcaption>As an additional manager, if you are added after some students have joined the group you won't have access to their data. Things may look quite like this!</figcaption>
</figure>

This can be remedied by asking all the students to re-enter the group code, which will list all the group managers and then give them all access. It's a possible issue that follows from our student-first permissions model, and shouldn't arise for new groups when additional managers are added as soon as a group is created.

Currently it's not possible to show only groups you own, or only assignments you have set to a group. We expect to find more improvements like these as we test things internally and hope that when we launch it as a beta feature we'll get further feedback too. We'll aim to improve things continually until we're happy it's ready for all teachers.

Note that you don't need the beta feature enabled to be added as an additional manager; if you have a teacher account and you're added, you'll just receive an email from Isaac to notify you.

Keep an eye on our <a href="https://twitter.com/isaacphysics" target="_blank">Twitter</a> for updates on this feature, or <a href="https://isaacphysics.org/contact?subject=Multiple%20Teachers%20per%20Group" target="_blank">get in touch with any questions here</a>!
