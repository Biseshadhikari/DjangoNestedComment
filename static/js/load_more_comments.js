  function toggleReplyForm(commentId) {
    const replyButton = document.querySelector(`[data-reply-button="replyBtn-${commentId}"]`);
    const cancelButton = document.querySelector(`[data-cancel-button="cancelBtn-${commentId}"]`);
    const replyForm = document.getElementById(`reply-form-${commentId}`);

    replyButton.classList.add('hidden');
    cancelButton.classList.remove('hidden');
    replyForm.classList.remove('hidden');
  }

  function cancelReply(commentId) {
    const replyButton = document.querySelector(`[data-reply-button="replyBtn-${commentId}"]`);
    const cancelButton = document.querySelector(`[data-cancel-button="cancelBtn-${commentId}"]`);
    const replyForm = document.getElementById(`reply-form-${commentId}`);

    replyButton.classList.remove('hidden');
    cancelButton.classList.add('hidden');
    replyForm.classList.add('hidden');
  }
