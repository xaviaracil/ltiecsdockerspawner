from ecsspawner.ecsspawner import ECSSpawner
from ltiauthenticator.lti_aware import LTIAwareMixin
from tornado import gen
from traitlets import Unicode

class LTIECSDockerSpawner(ECSSpawner, LTIAwareMixin):

    """
    ECSSpawner that defines notebook_dir and container_image
    from LTI (http://www.imsglobal.org/activity/learning-tools-interoperability) context
    """
    notebooks_git_repo = Unicode(
        '',
        config=True,
        allow_none=True,
        help="URL of a git repo where find notebooks for every context."
    )

    def _fmt(self, v):
        format_args = dict(
                context_id=self.provider.context_id,
                codi_tercers=self.provider.get_custom_param("domain_coditercers") # UOC only
        )

        return v.format(**format_args)

    def get_env(self):
        env = super().get_env()
        if self.notebooks_git_repo:
            git_repo_url = self._fmt(self.notebooks_git_repo)
            self.log.info(
                "notebooks_git_repo present with value %s. Formatted: %s",
                self.notebooks_git_repo, git_repo_url)
            env["NOTEBOOK_GIT_REPO"] = git_repo_url
            env["NOTEBOOK_GIT_DIR"] = self.provider.get_custom_param("domain_coditercers")

        return env
