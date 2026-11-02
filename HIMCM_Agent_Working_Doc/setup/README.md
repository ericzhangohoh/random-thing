# Set up the working document

Use the document directly. No skill installation, plugin, automated agent framework or GitHub connection is required to start.

1. Read [WORKING_DOC.md](../WORKING_DOC.md) and identify a separate active contest/practice project directory.
2. Follow [Claude Code setup](CLAUDE_CODE.md) to start a coordinator session and bounded worker sessions.
3. Use the [shared-directory protocol](SHARED_DIRECTORY_PROTOCOL.md) and copy/adapt the [assignment manifest](role_assignments.yaml.template) inside the active project.
4. Paste the [bootstrap prompt](BOOTSTRAP_PROMPT.md), then the relevant role assignment prompt from `roles/`.
5. Use [GitHub setup](GITHUB.md) for the chosen private repository arrangement and controlled versioning.

The files ending in `.template` are inert examples. They have not been installed into a project root or user configuration. The six optional native role definitions are also inert until deliberately copied. Neither this guide nor the role documents alter permissions, launch agents, create repositories or push changes by being read.

`DOC_ROOT` means this reusable working-document folder. `PROJECT_ROOT` means the active problem workspace. Keeping those names distinct prevents agents from writing current-contest results into the historical research corpus.

Configuration sources were checked on **2026-11-02**; see [source notes](SOURCES.md). Claude Code was not installed in the authoring environment, so the launch examples and optional definition were checked against current documentation and inspected statically, not live-tested in Claude Code. No installation was performed.
