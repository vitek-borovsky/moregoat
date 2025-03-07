import { configureStore, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";

// Define the state type
interface GlobalState {
  value: string;
}

// Initial state
const initialState: GlobalState = {
  value: "Hello World, from global state",
};

// Create a Redux slice
const globalSlice = createSlice({
  name: "global",
  initialState,
  reducers: {
    setValue: (state, action: PayloadAction<string>) => {
      state.value = action.payload;
    },
  },
});

// Export actions
export const { setValue } = globalSlice.actions;

// Create store
export const store = configureStore({
  reducer: {
    global: globalSlice.reducer,
  },
});

// Infer RootState and AppDispatch types from the store
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Custom hooks for TypeScript safety
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
