import { initializeApp } from 'firebase/app';
import { 
  getAuth, 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  User,
  GoogleAuthProvider,
  GithubAuthProvider,
  signInWithPopup,
  sendEmailVerification,
  sendPasswordResetEmail
} from 'firebase/auth';
import { 
  getFirestore, 
  doc, 
  setDoc, 
  getDoc, 
  updateDoc, 
  increment,
  collection,
  query,
  where,
  getDocs,
  Timestamp
} from 'firebase/firestore';
import { getStorage, ref as storageRef, uploadBytes, getDownloadURL } from 'firebase/storage';

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCBR5sd5kI8l-3WpNnL0J16t3SvqGi7lQg",
  authDomain: "henu-586ce.firebaseapp.com",
  databaseURL: "https://henu-586ce-default-rtdb.firebaseio.com",
  projectId: "henu-586ce",
  storageBucket: "henu-586ce.firebasestorage.app",
  messagingSenderId: "633755919625",
  appId: "1:633755919625:web:3a86a50604c1e143495fd8",
  measurementId: "G-GTVCJE7M5T"
};

// OAuth configuration
const googleOAuthConfig = {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID || "756347539673-tm61v3l1peq6uena8tcekpri57l7aktr.apps.googleusercontent.com",
  clientSecret: import.meta.env.VITE_GOOGLE_CLIENT_SECRET || "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"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const googleProvider = new GoogleAuthProvider();
const githubProvider = new GithubAuthProvider();
const storage = getStorage(app);

// User interface
interface UserData {
  uid: string;
  email: string;
  displayName?: string;
  photoURL?: string;
  role: 'free' | 'premium';
  emailVerified: boolean;
  downloadCount: number;
  lastDownloadDate?: Timestamp;
  createdAt: Timestamp;
  updatedAt: Timestamp;
}

// Authentication functions
export const signInWithGoogle = async () => {
  try {
    googleProvider.addScope('email');
    googleProvider.addScope('profile');
    googleProvider.setCustomParameters({
      client_id: googleOAuthConfig.clientId
    });
    
    const result = await signInWithPopup(auth, googleProvider);
    
    // Create or update user data
    await createOrUpdateUser(result.user);
    
    return { user: result.user, error: null };
  } catch (error: any) {
    return { user: null, error: error.message };
  }
};

export const signInWithGitHub = async () => {
  try {
    githubProvider.addScope('user:email');
    
    const result = await signInWithPopup(auth, githubProvider);
    
    // Create or update user data
    await createOrUpdateUser(result.user);
    
    return { user: result.user, error: null };
  } catch (error: any) {
    return { user: null, error: error.message };
  }
};

export const signInWithEmail = async (email: string, password: string) => {
  try {
    const result = await signInWithEmailAndPassword(auth, email, password);
    return { user: result.user, error: null };
  } catch (error: any) {
    return { user: null, error: error.message };
  }
};

export const signUpWithEmail = async (email: string, password: string) => {
  try {
    const result = await createUserWithEmailAndPassword(auth, email, password);
    
    // Send email verification
    await sendEmailVerification(result.user);
    
    // Create user data
    await createOrUpdateUser(result.user);
    
    return { user: result.user, error: null };
  } catch (error: any) {
    return { user: null, error: error.message };
  }
};

export const signOutUser = async () => {
  try {
    await signOut(auth);
    return { error: null };
  } catch (error: any) {
    return { error: error.message };
  }
};

export const sendPasswordReset = async (email: string) => {
  try {
    await sendPasswordResetEmail(auth, email);
    return { error: null };
  } catch (error: any) {
    return { error: error.message };
  }
};

// User management functions
export const createOrUpdateUser = async (user: User) => {
  try {
    console.log('Creating/updating user:', user.uid);
    const userRef = doc(db, 'users', user.uid);
    const userSnap = await getDoc(userRef);
    
    const now = Timestamp.now();
    
    if (!userSnap.exists()) {
      // Create new user
      const userData: any = {
        uid: user.uid,
        email: user.email || '',
        displayName: user.displayName || undefined,
        photoURL: user.photoURL || undefined,
        role: 'free',
        emailVerified: user.emailVerified,
        downloadCount: 0,
        createdAt: now,
        updatedAt: now
      };
      // Only add lastDownloadDate if it is defined
      // (for new users, don't include it at all)
      // Save userData
      await setDoc(userRef, userData);
      console.log('User data created successfully');
    } else {
      // Update existing user
      console.log('Updating existing user');
      await updateDoc(userRef, {
        email: user.email,
        displayName: user.displayName,
        photoURL: user.photoURL,
        emailVerified: user.emailVerified,
        updatedAt: now
      });
      console.log('User data updated successfully');
    }
  } catch (error) {
    console.error('Error creating/updating user:', error);
    throw error;
  }
};

export const getUserData = async (uid: string): Promise<UserData | null> => {
  try {
    console.log('Getting user data for:', uid);
    const userRef = doc(db, 'users', uid);
    const userSnap = await getDoc(userRef);
    
    if (userSnap.exists()) {
      const userData = userSnap.data() as UserData;
      console.log('User data found:', userData);
      return userData;
    } else {
      console.log('No user data found for UID:', uid);
      return null;
    }
  } catch (error) {
    console.error('Error getting user data:', error);
    return null;
  }
};

export const checkDownloadLimit = async (uid: string): Promise<{ canDownload: boolean; remainingDownloads: number; error?: string }> => {
  try {
    const userData = await getUserData(uid);
    
    if (!userData) {
      return { canDownload: false, remainingDownloads: 0, error: 'User data not found' };
    }
    
    // Check if user is verified
    if (!userData.emailVerified) {
      return { canDownload: false, remainingDownloads: 0, error: 'Please verify your email address first' };
    }
    
    // Check daily download limit (3 downloads per day for free users)
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    const downloadsToday = await getDownloadsToday(uid, today);
    const maxDownloads = userData.role === 'premium' ? 10 : 3;
    const remainingDownloads = Math.max(0, maxDownloads - downloadsToday);
    
    return {
      canDownload: remainingDownloads > 0,
      remainingDownloads
    };
  } catch (error) {
    console.error('Error checking download limit:', error);
    return { canDownload: false, remainingDownloads: 0, error: 'Failed to check download limit' };
  }
};

export const recordDownload = async (uid: string): Promise<{ success: boolean; error?: string }> => {
  try {
    const userRef = doc(db, 'users', uid);
    
    // Update user download count
    await updateDoc(userRef, {
      downloadCount: increment(1),
      lastDownloadDate: Timestamp.now()
    });
    
    // Record download in downloads collection
    const downloadRef = doc(collection(db, 'downloads'));
    await setDoc(downloadRef, {
      uid,
      timestamp: Timestamp.now(),
      userAgent: navigator.userAgent,
      ip: 'client-side' // In production, this would be set server-side
    });
    
    return { success: true };
  } catch (error) {
    console.error('Error recording download:', error);
    return { success: false, error: 'Failed to record download' };
  }
};

const getDownloadsToday = async (uid: string, today: Date): Promise<number> => {
  try {
    const downloadsRef = collection(db, 'downloads');
    const q = query(
      downloadsRef,
      where('uid', '==', uid),
      where('timestamp', '>=', Timestamp.fromDate(today))
    );
    
    const querySnapshot = await getDocs(q);
    return querySnapshot.size;
  } catch (error) {
    console.error('Error getting downloads today:', error);
    return 0;
  }
};

export const saveTeamApplication = async (data: {
  name: string;
  phone: string;
  email: string;
  address: string;
  skills: string[];
  photoBase64?: string;
  photoName?: string;
  resumeBase64?: string;
  resumeName?: string;
  submittedAt?: any;
}) => {
  try {
    const db = getFirestore();
    const applicationsRef = collection(db, 'team_applications');
    await setDoc(doc(applicationsRef), {
      ...data,
      submittedAt: data.submittedAt || Timestamp.now(),
    });
    return { success: true };
  } catch (error) {
    console.error('Error saving team application:', error);
    return { success: false, error: error.message };
  }
};

export const getCurrentUser = (): User | null => {
  return auth.currentUser;
};

export const onAuthStateChange = (callback: (user: User | null) => void) => {
  return onAuthStateChanged(auth, callback);
};

export { auth, db }; 

// Helper to upload a file and return its download URL
export const uploadFileAndGetURL = async (file: File, path: string): Promise<string> => {
  const fileRef = storageRef(storage, path);
  await uploadBytes(fileRef, file);
  return await getDownloadURL(fileRef);
}; 