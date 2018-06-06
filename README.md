# isaac-labs

The technical blog for [Isaac Physics](https://isaacphysics.org). Runs Jekyll in a Docker container.

### Development Setup Instructions

1. Install Docker
2. Clone this repository
3. Run `./run.sh`

Your server should be running locally at `http://localhost:4000`.

### Adding Posts

To add a new post to the blog, create a new file in the `_posts` directory with a filename matching the `YYYY-MM-DD-some-title.markdown`. The file should contain a YAML header describing the post, use an existing post as a template. If the post is not yet ready, you can add `draft: true` to this YAML section. Once saved, you'll find the new post at `http://localhost:4000/some-title.html`. Images should be added in the `images` directory, other configuration should not need to be modified.

### Production Use

When running in production, do not use `./run.sh`. Instead just use `docker-compose up -d`. The `docker-compose.yml` file contains all the correct configuration for this use.
