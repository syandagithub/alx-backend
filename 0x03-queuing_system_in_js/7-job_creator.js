#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '41535187',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '41535781',
    message: 'This is the code 456 to verify your account',
  },
  {
    phoneNumber: '41538743',
    message: 'This is the code 432 to verify your account',
  },
  {
    phoneNumber: '41538781',
    message: 'This is the code 452 to verify your account',
  },
  {
    phoneNumber: '41531182',
    message: 'This is the code 431 to verify your account',
  },
  {
    phoneNumber: '41537781',
    message: 'This is the code 462 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  job.save();
}
